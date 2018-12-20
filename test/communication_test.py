# -*- coding: utf-8 -*-

from communication.message import Message
from communication.message_processing import MSGProcessing


if __name__ == '__main__':
    msg = Message('ns3', False, [0, 1], 0, [1, 1, 1, 1], None, 10, 1, False)
    result = MSGProcessing.send(msg)
    print result
    result = MSGProcessing.receive(result)
    print result
    print result.game_name
    print result.is_reset
    print result.action_space
    print result.action
    print result.initial_observation
    print result.observation
    print result.num_features
    print result.reward
    print result.is_terminal
