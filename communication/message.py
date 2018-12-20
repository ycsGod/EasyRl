# -*- coding: utf-8 -*-


class Message(object):
    def __init__(self,
                 env_id=None,
                 game_name=None,
                 is_reset=False,
                 action_space=None,
                 action=None,
                 initial_observation=None,
                 observation=None,
                 num_features=None,
                 reward=None,
                 is_terminal=False):
        self._env_id = str(env_id)  # 环境的唯一标识符

        self._game_name = game_name  # 用于创建环境的环境名称
        self._is_reset = is_reset  # 用于将环境初始化
        self._action_space = action_space  # 环境的动作空间
        self._action = action  # agent选取的动作
        self._initial_observation = str(initial_observation)  # 环境的初始状态
        self._observation = str(observation)  # 环境执行某一个动作之后的下一个状态
        self._num_features = num_features  # 环境状态的特征数量
        self._reward = reward  # 环境执行某一个动作之后的奖励
        self._is_terminal = is_terminal  # 环境是否终止

    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        self._env_id = str(env_id)

    @property
    def is_reset(self):
        return self._is_reset

    @is_reset.setter
    def is_reset(self, is_reset):
        self._is_reset = is_reset

    @property
    def action_space(self):
        return self._action_space

    @action_space.setter
    def action_space(self, action_space):
        self._action_space = action_space

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    @property
    def game_name(self):
        return self._game_name

    @game_name.setter
    def game_name(self, game_name):
        self._game_name = game_name

    @property
    def initial_observation(self):
        return self._initial_observation

    @initial_observation.setter
    def initial_observation(self, initial_observation):
        self._initial_observation = str(initial_observation)

    @property
    def observation(self):
        return self._observation

    @observation.setter
    def observation(self, observation):
        self._observation = str(observation)

    @property
    def num_features(self):
        return self._num_features

    @num_features.setter
    def num_features(self, num_features):
        self._num_features = num_features

    @property
    def reward(self):
        return self._reward

    @reward.setter
    def reward(self, reward):
        self._reward = reward

    @property
    def is_terminal(self):
        return self._is_terminal

    @is_terminal.setter
    def is_terminal(self, is_terminal):
        self._is_terminal = is_terminal
