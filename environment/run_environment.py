# -*- coding: utf-8 -*-

from EasyRL.communication.message_processing import MSGProcessing
from EasyRL.communication.message import Message


class Runner(object):
    def __init__(self,
                 create_agent_function,
                 game_name=None,
                 episodes=200,
                 max_steps_per_episode=27000):
        assert game_name is not None

        self._env_id = None
        self._episode = episodes
        self._max_steps_per_episode = max_steps_per_episode

        self._agent = create_agent_function(self._create_env_function(game_name))

    def _create_env_function(self, game_name):
        msg = Message(game_name=game_name)
        result = MSGProcessing.send(MSGProcessing.CREATE_ENV_URL, msg)
        msg = MSGProcessing.deserialization(result)
        self._env_id = msg.env_id
        return msg.action_space

    def _env_reset(self):
        msg = Message(env_id=self._env_id, is_reset=True)
        result = MSGProcessing.send(MSGProcessing.RESET_ENV_URL, msg)
        msg = MSGProcessing.deserialization(result)
        return msg.initial_observation

    def _env_step(self, action):
        msg = Message(env_id=self._env_id, action=action)
        result = MSGProcessing.send(MSGProcessing.ENV_STEP_URL, msg)
        msg = MSGProcessing.deserialization(result)
        return msg.observation, msg.reward, msg.is_terminal

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
            # 环境执行action，返回observation, reward和终止状态
            observation, reward, is_terminal = self._run_one_step(action)

            step_number += 1

            if is_terminal or step_number == self._max_steps_per_episode:
                break
            else:
                # 更新ｑ表，返回下一步action
                action = self._agent.step(reward, observation)

        print "Steps executed: {}".format(step_number)

    def destroy_env(self):
        msg = Message(env_id=self._env_id)
        MSGProcessing.send(MSGProcessing.ENV_STOP_URL, msg)

    def run(self):
        print "Beginning training......"
        for episode in range(0, self._episode):
            self._run_one_episode(episode)
        self.destroy_env()
