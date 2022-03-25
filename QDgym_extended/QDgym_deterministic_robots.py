import gym
gym.logger.set_level(40)
import numpy as np
import pybullet
from pybullet_envs.gym_locomotion_envs import Ant, HalfCheetah, Walker2D, Humanoid, Hopper


class DeterministicAnt(Ant):
    def robot_specific_reset(self, bullet_client):
        super().robot_specific_reset(bullet_client)
        for j in self.ordered_joints:
            j.reset_current_position(0, 0)

class DeterministicHalfCheetah(HalfCheetah):
    def robot_specific_reset(self, bullet_client):
        super().robot_specific_reset(bullet_client)
        for j in self.ordered_joints:
            j.reset_current_position(0, 0)

class DeterministicWalker2D(Walker2D):
    def robot_specific_reset(self, bullet_client):
        super().robot_specific_reset(bullet_client)
        for j in self.ordered_joints:
            j.reset_current_position(0, 0)

class DeterministicHumanoid(Humanoid):
    random_yaw = False
    random_lean = False
    def robot_specific_reset(self, bullet_client):
        super().robot_specific_reset(bullet_client)
        for j in self.ordered_joints:
            j.reset_current_position(0, 0)

class DeterministicHopper(Hopper):
    def robot_specific_reset(self, bullet_client):
        super().robot_specific_reset(bullet_client)
        for j in self.ordered_joints:
            j.reset_current_position(0, 0)

