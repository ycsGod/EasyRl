# -*- coding: utf-8 -*-

from communication.message import Message
from communication.message_processing import MSGProcessing


if __name__ == '__main__':
    msg = Message(game_name='MountainCar-v0')
    result = MSGProcessing.send(MSGProcessing.CREATE_ENV_URL, msg)
    action_space = result.action_space
    print action_space[0]
    env_id = result.env_id
    print env_id

    msg = Message(env_id=env_id, is_reset=True)
    result = MSGProcessing.send(MSGProcessing.RESET_ENV_URL, msg)
    print result.initial_observation

    msg = Message(env_id=env_id, action=0)
    result = MSGProcessing.send(MSGProcessing.ENV_STEP_URL, msg)
    observation = result.observation
    reward = result.observation
    is_terminal = result.is_terminal
    print "observation: {}, reward: {}, is_terminal: {}".format(observation, reward, is_terminal)

    msg = Message(env_id=env_id)
    result = MSGProcessing.send(MSGProcessing.ENV_STOP_URL, msg)
    if result.is_terminal:
        print "game over!"