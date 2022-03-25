import logging
import gym
from gym.envs.registration import registry, make, spec

from .QDgym_deterministic_robots import DeterministicAnt, DeterministicHalfCheetah, DeterministicWalker2D, DeterministicHumanoid, DeterministicHopper

def register(id, *args, **kvargs):
  if id in registry.env_specs:
    return
  else:
    return gym.envs.registration.register(id, *args, **kvargs)


# ------------QDgym-------------

register(id='QDWalker2DBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_envs:QDWalker2DBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)


register(id='QDHalfCheetahBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_envs:QDHalfCheetahBulletEnv',
         max_episode_steps=1000,
         reward_threshold=3000.0)


register(id='QDAntBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_envs:QDAntBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)


register(id='QDHopperBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_envs:QDHopperBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)


register(id='QDHumanoidBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_envs:QDHumanoidBulletEnv',
         max_episode_steps=1000)


# ------------QDgym-deterministic-------------

register(id='QDDeterministicWalker2DBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_deterministic_envs:QDDeterministicWalker2DBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)


register(id='QDDeterministicHalfCheetahBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_deterministic_envs:QDDeterministicHalfCheetahBulletEnv',
         max_episode_steps=1000,
         reward_threshold=3000.0)


register(id='QDDeterministicAntBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_deterministic_envs:QDDeterministicAntBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)


register(id='QDDeterministicHopperBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_deterministic_envs:QDDeterministicHopperBulletEnv',
         max_episode_steps=1000,
         reward_threshold=2500.0)

register(id='QDDeterministicHumanoidBulletEnv-v0',
         entry_point='QDgym_extended.QDgym_deterministic_envs:QDDeterministicHumanoidBulletEnv',
	 max_episode_steps=1000)



def getList():
  btenvs = ['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.find('QD') >= 0]
  return btenvs
