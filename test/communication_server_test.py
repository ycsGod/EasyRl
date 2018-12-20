# -*- coding: utf-8 -*-

from flask import Flask, request
from EasyRL.communication.message import Message
from EasyRL.communication.message_processing import MSGProcessing
import gym
from EasyRL.environment.environment_manager import EnvManager

app = Flask(__name__)

env_list = {}


@app.route('/create_env', methods=['POST'])
def create_env():
    msg = MSGProcessing.deserialization(request.data)
    game_name = msg.game_name
    print "game_name: {}".format(game_name)
    env = gym.make(game_name)
    print "action_space: {}".format(list(range(0, env.action_space.n)))
    env_id = id_manager.create_id()
    print "env_id: {}".format(env_id)
    env_dict[env_id] = env
    msg = Message(env_id=env_id, action_space=list(range(0, env.action_space.n)))
    return MSGProcessing.serialization(msg)


@app.route('/reset_env', methods=['POST'])
def reset_env():
    msg = MSGProcessing.deserialization(request.data)
    assert msg.is_reset is True
    env_id = msg.env_id
    env = env_dict[env_id]
    initial_observation = env.reset()
    msg = Message(env_id=env_id, initial_observation=initial_observation)
    return MSGProcessing.serialization(msg)


if __name__ == '__main__':
    id_manager = EnvManager()
    env_dict = {}
    app.run(debug=True)
