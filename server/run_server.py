# -*- coding: utf-8 -*-

from flask import Flask, request
from communication.message_processing import MSGProcessing
from communication.message import Message
import gym
from environment.environment_manager import EnvManager

app = Flask(__name__)


@app.route('/create_env', methods=['POST'])
def create_env():
    env = gym.make(MSGProcessing.deserialization(request.data).game_name)
    env_id = env_manager.add_env(env)
    msg = Message(env_id=env_id, action_space=list(range(0, env.action_space.n)))
    return MSGProcessing.serialization(msg)


@app.route('/reset_env', methods=['POST'])
def reset_env():
    msg = MSGProcessing.deserialization(request.data)
    assert msg.is_reset is True
    env_id = msg.env_id
    env = env_manager.env_dict[env_id]
    initial_observation = env.reset()
    msg = Message(env_id=env_id, initial_observation=initial_observation)
    return MSGProcessing.serialization(msg)


@app.route('/env_step', methods=['POST'])
def env_step():
    msg = MSGProcessing.deserialization(request.data)
    action = msg.action
    # print "action: {}".format(action)
    env_id = msg.env_id
    # print "env_id: {}".format(env_id)
    env = env_manager.env_dict[env_id]
    observation, reward, is_terminal, _ = env.step(action)
    msg = Message(observation=observation, reward=reward, is_terminal=is_terminal)
    return MSGProcessing.serialization(msg)


@app.route('/env_stop', methods=['POST'])
def env_stop():
    env_id = MSGProcessing.deserialization(request.data).env_id
    env = env_manager.env_dict[env_id]
    env.close()
    env_manager.delete_env(env_id)
    msg = Message(env_id=env_id, is_terminal=True)
    return MSGProcessing.serialization(msg)


@app.route('/env_render', methods=['POST'])
def env_render():
    env_id = MSGProcessing.deserialization(request.data).env_id
    env = env_manager.env_dict[env_id]
    env.render()
    msg = Message(env_id=env_id)
    return MSGProcessing.serialization(msg)


if __name__ == '__main__':
    env_manager = EnvManager()
    app.run(debug=True)
