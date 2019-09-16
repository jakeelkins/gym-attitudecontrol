from gym.envs.registration import register

register(
    id='AttitudeControl-v0',
    entry_point='gym_attitudecontrol.envs:AttitudeControlEnv',
)
