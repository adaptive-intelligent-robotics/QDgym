import gym
gym.logger.set_level(40)
import numpy as np
from pybullet_envs.gym_locomotion_envs import WalkerBaseBulletEnv

from . import DeterministicAnt, DeterministicHalfCheetah, DeterministicWalker2D, DeterministicHumanoid, DeterministicHopper

class QDDeterministicAntBulletEnv(WalkerBaseBulletEnv):
    def __init__(self, render=False):
        self.robot = DeterministicAnt()
        super().__init__(self.robot, render=render)
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(4)])
        self.desc_acc = np.array([0.0 for _ in range(4)])

        print(f"The behavioural desciptor is {len(self.desc)}-dimentional",
              f"and defined as proportion of feet contact time with the ground in the order {self.robot.foot_list}")


    def reset(self):
        r = super().reset()
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(4)])
        self.desc_acc = np.array([0.0 for _ in range(4)])

        return r

    
    def step(self, a):
        state, reward, done, info = super().step(a)
        self.desc_acc += self.robot.feet_contact
        self.tot_reward += reward
        self.T += 1
        self.alive = (self.__dict__["_alive"] >= 0.0)
        self.desc = self.desc_acc / self.T
        info["bc"] = self.desc
        info["x_pos"] = None
        return state, reward, done, info



class QDDeterministicHalfCheetahBulletEnv(WalkerBaseBulletEnv):
    def __init__(self, render=False):
        self.robot = DeterministicHalfCheetah()
        super().__init__(self.robot, render=render)
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])
        self.desc_acc = np.array([0.0 for _ in range(2)])

        print(f"The behavioural desciptor is {len(self.desc)}-dimentional",
              f"and defined as proportion of feet contact time with the ground in the order {[self.robot.foot_list[0] , self.robot.foot_list[3]]}")


    def reset(self):
        r = super().reset()
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])
        self.desc_acc = np.array([0.0 for _ in range(2)])

        return r

    
    def step(self, a):
        state, reward, done, info = super().step(a)
        self.desc_acc[0] += self.robot.feet_contact[0]
        self.desc_acc[1] += self.robot.feet_contact[3]
        self.tot_reward += reward
        self.T += 1
        self.alive = (self.__dict__["_alive"] >= 0.0)
        self.desc = self.desc_acc / self.T
        info["bc"] = self.desc
        info["x_pos"] = None
        return state, reward, done, info



class QDDeterministicWalker2DBulletEnv(WalkerBaseBulletEnv):
    def __init__(self, render=False):
        self.robot = DeterministicWalker2D()
        super().__init__(self.robot, render=render)
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])
        self.desc_acc = np.array([0.0 for _ in range(2)])

        print(f"The behavioural desciptor is {len(self.desc)}-dimentional",
              f"and defined as proportion of feet contact time with the ground in the order {self.robot.foot_list}")


    def reset(self):
        r = super().reset()
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])
        self.desc_acc = np.array([0.0 for _ in range(2)])

        return r

    
    def step(self, a):
        state, reward, done, info = super().step(a)
        self.desc_acc += self.robot.feet_contact
        self.tot_reward += reward
        self.T += 1
        self.alive = (self.__dict__["_alive"] >= 0.0)
        self.desc = self.desc_acc / self.T
        info["bc"] = self.desc
        info["x_pos"] = None
        return state, reward, done, info



class QDDeterministicHumanoidBulletEnv(WalkerBaseBulletEnv):
    def __init__(self, render=False):
        self.robot = DeterministicHumanoid()
        super().__init__(self.robot, render=render)
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])
        self.desc_acc = np.array([0.0 for _ in range(2)])

        print(f"The behavioural desciptor is {len(self.desc)}-dimentional",
              f"and defined as proportion of feet contact time with the ground in the order {self.robot.foot_list}")


    def reset(self):
        r = super().reset()
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(2)])
        self.desc_acc = np.array([0.0 for _ in range(2)])

        return r

    
    def step(self, a):
        state, reward, done, info = super().step(a)
        self.desc_acc += self.robot.feet_contact
        self.tot_reward += reward
        self.T += 1
        self.alive = (self.__dict__["_alive"] >= 0.0)
        self.desc = self.desc_acc / self.T
        info["bc"] = self.desc
        info["x_pos"] = None
        return state, reward, done, info



class QDDeterministicHopperBulletEnv(WalkerBaseBulletEnv):
    def __init__(self, render=False):
        self.robot = DeterministicHopper()
        super().__init__(self.robot, render=render)
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(1)])
        self.desc_acc = np.array([0.0 for _ in range(1)])

        print(f"The behavioural desciptor is {len(self.desc)}-dimentional",
              f"and defined as proportion of feet contact time with the ground in the order {self.robot.foot_list}")


    def reset(self):
        r = super().reset()
        self.T = 0
        self.tot_reward = 0.0
        self.desc = np.array([0.0 for _ in range(1)])
        self.desc_acc = np.array([0.0 for _ in range(1)])

        return r

    
    def step(self, a):
        state, reward, done, info = super().step(a)
        self.desc_acc += self.robot.feet_contact
        self.tot_reward += reward
        self.T += 1
        self.alive = (self.__dict__["_alive"] >= 0.0)
        self.desc = self.desc_acc / self.T
        info["bc"] = self.desc
        info["x_pos"] = None
        return state, reward, done, info



if __name__ == "__main__":
    env = QDDeterministicHalfCheetahBulletEnv()
    env.reset()
    a = env.action_space.sample()
    env.step(a)
    print(env.alive)
    print(env.desc)
