# -*- coding: utf-8 -*-

from communication.message_processing import MSGProcessing
from communication.message import Message
from communication.config import Config


class Runner(object):
    def __init__(self,
                 config,
                 create_agent_function,
                 game_name=None,
                 episodes=2000,
                 max_steps_per_episode=27000):
        assert game_name is not None

        self._config = config
        self._env_id = None
        self._episode = episodes
        self._max_steps_per_episode = max_steps_per_episode

        self._agent = create_agent_function(self._create_env_function(game_name))

    def _create_env_function(self, game_name):
        msg = Message(game_name=game_name)
        result = MSGProcessing.send(self._config.create_env_url, msg)
        self._env_id = result.env_id
        return result.action_space

    def _env_reset(self):
        msg = Message(env_id=self._env_id, is_reset=True)
        result = MSGProcessing.send(self._config.reset_env_url, msg)
        return result.initial_observation

    def _env_step(self, action):
        msg = Message(env_id=self._env_id, action=action)
        result = MSGProcessing.send(self._config.env_step_url, msg)
        return result.observation, result.reward, result.is_terminal

    def _initial_episode(self):
        initial_observation = self._env_reset()
        return self._agent.begin_episode(initial_observation)

    def _run_one_step(self, action):
        observation, reward, is_terminal = self._env_step(action)
        return observation, reward, is_terminal

    def _run_one_episode(self, episode):
        print "Episode: {}".format(episode)
        step_number = 0

        # 获取环境的初始state,并且选取初始的action
        action = self._initial_episode()

        while True:
            # self.env_render()

            # 环境执行action，返回observation, reward和终止状态
            observation, reward, is_terminal = self._run_one_step(action)

            step_number += 1

            if is_terminal or step_number == self._max_steps_per_episode:
                break
            else:
                action = self._agent.step(reward, observation)

        print "Steps executed: {}".format(step_number)

    def destroy_env(self):
        msg = Message(env_id=self._env_id)
        MSGProcessing.send(self._config.env_stop_url, msg)

    def env_render(self):
        msg = Message(env_id=self._env_id)
        MSGProcessing.send(self._config.env_render_url, msg)

    def run(self):
        print "Beginning training......"
        for episode in range(0, self._episode):
            self._run_one_episode(episode)
        self.destroy_env()
