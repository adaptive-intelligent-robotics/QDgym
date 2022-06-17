import gym
import numpy as np

from pybullet_envs.gym_locomotion_envs import WalkerBaseBulletEnv
from pybullet_envs.robot_locomotors import Ant, WalkerBase

#| Author: Bryan Lim
#| Editing: Manon Flageat

# Robot OmnidirectionalAnt 
class OmnidirectionalAnt(Ant):

    def __init__(self, do_consider_xy_pos=False):
        self.do_consider_xy_pos = do_consider_xy_pos # Consider x,y position in observation
        if not self.do_consider_xy_pos:
            obs_dim = 28
        else:
            obs_dim = 28 + 2

        WalkerBase.__init__(self, "ant.xml", "torso", action_dim=8, obs_dim=obs_dim, power=2.5)

    def robot_specific_reset(self, bullet_client):
        self.initial_x = None
        self.initial_y = None
        Ant.robot_specific_reset(self, bullet_client)

    def calc_state(self):
        """
        Get the state of the robot.
        """

        # Get joint position and velocity
        joints_pos_vel = np.array([j.current_relative_position() for j in self.ordered_joints],
                                  dtype=np.float32).flatten()

        # even elements [0::2] position, scaled to -1..+1
        # odd elements  [1::2] angular speed, scaled to -1..+1
        self.joint_speeds = joints_pos_vel[1::2]
        self.joints_at_limit = np.count_nonzero(np.abs(joints_pos_vel[0::2]) > 0.99)

        # Get body position
        body_pose = self.robot_body.pose()
        parts_xyz = np.array([p.pose().xyz() for p in self.parts.values()]).flatten()
        self.body_xyz = (parts_xyz[0::3].mean(), parts_xyz[1::3].mean(), body_pose.xyz()[2]
                         )  # torso z is more informative than mean z
        self.body_real_xyz = body_pose.xyz()
        self.body_rpy = body_pose.rpy()

        # Set initial body position
        x, y, z = self.body_xyz
        if self.initial_x is None:
            self.initial_x = x
        if self.initial_y is None:
            self.initial_y = y
        if self.initial_z is None:
            self.initial_z = z

        # Get body angular position and velocity
        roll, pitch, yaw = self.body_rpy
        rot_speed = np.array([[np.cos(-yaw), -np.sin(-yaw), 0], [np.sin(-yaw),
                                                                 np.cos(-yaw), 0], [0, 0, 1]])
        vx, vy, vz = np.dot(rot_speed,
                            self.robot_body.speed())  # rotate speed back to body point of view

        # Sum up all information to get final observation
        more = np.array(
            [
                z - self.initial_z,
                np.sin(yaw),
                np.cos(yaw),
                0.3 * vx,
                0.3 * vy,
                0.3 * vz,  # 0.3 is just scaling typical speed into -1..+1, no physical sense here
                roll,
                pitch
            ],
            dtype=np.float32)

        if self.do_consider_xy_pos:
            supplementary_state_info = np.array(
                [
                    x - self.initial_x,
                    y - self.initial_y,
                ],
                dtype=np.float32
            )
        else:
            supplementary_state_info = np.array([], dtype=np.float32)

        return np.clip(np.concatenate([more]
                                      + [supplementary_state_info]
                                      + [joints_pos_vel]
                                      + [self.feet_contact]),
                       -5, +5)

    def calc_potential(self):
        """
        Get the reward of the robot.
        """
        return -1.  # No trivial reward for omnidirectional task.


# Bullet standard OmnidirectionalAntBulletEnv environment
class OmnidirectionalAntBulletEnv(WalkerBaseBulletEnv):
    PRIOR_STATE_INFORMATION = "prior_state_information"

    def __init__(self, render=False, do_consider_xy_pos=False):
        self.robot = OmnidirectionalAnt(do_consider_xy_pos)
        self.do_consider_xy_pos = do_consider_xy_pos
        WalkerBaseBulletEnv.__init__(self, self.robot, render)

    def step(self, a):
        state, reward, done, info_dict = super(OmnidirectionalAntBulletEnv, self).step(a)

        x, y, _ = self.robot.body_xyz
        prior_state_information = np.array([
            x, y
        ], dtype=np.float32)

        info_dict.update({
            self.PRIOR_STATE_INFORMATION: prior_state_information
        })

        return state, reward, done, info_dict


# QD version of OmnidirectionalAntBulletEnv
class QDAntOmnidirectionalBulletEnv(OmnidirectionalAntBulletEnv):
    def __init__(self, render=False):
        super().__init__(render=render, do_consider_xy_pos=True)
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)]) 
        self.min_desc = [-4, -4]
        self.max_desc = [4, 4]

        print(f"The behavioural desciptor is {len(self.desc)}-dimentional",
              f"and defined as the final x,y position of the robot CoM")

    def reset(self):
        r = super().reset()
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])

        return r
    
    def step(self, a):
        state, reward, done, info = super().step(a)
        self.tot_reward += reward
        self.T += 1
        self.alive = (self.__dict__["_alive"] >= 0.0)
        self.desc = np.clip(np.array([(state[8] - self.min_desc[0]) / (self.max_desc[0] - self.min_desc[0]), 
                                      (state[9] - self.min_desc[1]) / (self.max_desc[1] - self.min_desc[1])]), 0, 1)
        info["bc"] = self.desc
        info["x_pos"] = None
        return state, reward, done, info

