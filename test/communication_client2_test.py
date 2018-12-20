# -*- coding: utf-8 -*-

from EasyRL.communication.message import Message
from EasyRL.communication.message_processing import MSGProcessing


if __name__ == '__main__':
    msg = Message(game_name='MountainCar-v0')
    result = MSGProcessing.send(MSGProcessing.CREATE_ENV_URL, msg)
    msg = MSGProcessing.deserialization(result)
    print msg.action_space
    env_id = msg.env_id
    print env_id

    msg = Message(env_id=env_id, is_reset=True)
    result = MSGProcessing.send(MSGProcessing.RESET_ENV_URL, msg)
    print MSGProcessing.deserialization(result).initial_observation