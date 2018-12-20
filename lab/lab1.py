# -*- coding: utf-8 -*-

from agent.q_learning.q_leaning import QLearningTable
from environment.run_environment import Runner
from communication.config import Config


def create_agent_function(actions):
    return QLearningTable(actions=actions)


if __name__ == '__main__':
    config = Config()
    environment = Runner(config, create_agent_function, game_name="CartPole-v0")
    environment.run()