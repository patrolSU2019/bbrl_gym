from ._version import __version__, __version_tuple__
from gymnasium.envs.registration import register

register(
    id="CartPoleContinuous-v0",
    entry_point="bbrl_gym.envs:ContinuousCartPoleEnv",
    max_episode_steps=200,
    apply_api_compatibility=True,
)
register(
    id="CartPoleContinuous-v1",
    entry_point="bbrl_gym.envs:ContinuousCartPoleEnv",
    max_episode_steps=500,
    apply_api_compatibility=True,
)

register(id="LineMDP-v0", entry_point="bbrl_gym.envs:LineMDPEnv", max_episode_steps=100)
register(
    id="LineMDPContinuous-v0",
    entry_point="bbrl_gym.envs:ContinuousLineMDPEnv",
    max_episode_steps=100,
    apply_api_compatibility=True,
)
register(
    id="2DMDPContinuous-v0",
    entry_point="bbrl_gym.envs:Continuous2DMDPEnv",
    max_episode_steps=100,
    apply_api_compatibility=True,
)
register(
    id="RocketLander-v0",
    entry_point="bbrl_gym.envs:RocketLanderEnv",
    max_episode_steps=1000,
    reward_threshold=0,
    apply_api_compatibility=True,
)
register(id="MazeMDP-v0", entry_point="bbrl_gym.envs:MazeMDPEnv", max_episode_steps=1000, apply_api_compatibility=True)
register(id="DebugV-v0", entry_point="bbrl_gym.envs:DebugVEnv", max_episode_steps=10, apply_api_compatibility=True)
