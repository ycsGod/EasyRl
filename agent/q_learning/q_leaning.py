# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


class QLearningTable(object):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # 动作空间
        self.alpha = learning_rate  # 学习率
        self.gamma = reward_decay  # 奖励衰减值
        self.epsilon = e_greedy  # 动作选择贪婪度
        self._current_action = None
        self._current_observation = None

        # 初始化Q表(初始化的Q表是一个空表)
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    # 选取动作
    def choose_action(self):
        self.check_state_exist(self._current_observation)

        # 根据贪婪度选择动作
        if np.random.uniform() < self.epsilon:
            state_action = self.q_table.loc[self._current_observation, :]
            # 从拥有最大Q_value值的一系列actions中随机选择一个action
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            action = np.random.choice(self.actions)
        return action

    # 更新Q表
    def step(self, reward, observation_):
        self.check_state_exist(observation_)
        # Q估计
        q_predict = self.q_table.loc[self._current_observation, self._current_action]
        # Q现实
        if observation_ == "terminal":
            q_target = reward
        else:
            q_target = reward + self.gamma*self.q_table.loc[observation_, :].max()
        # Q表更新
        self.q_table.loc[self._current_observation, self._current_action] += self.alpha*(q_target - q_predict)

        # 需要返回动作
        self._current_observation = observation_
        return self.choose_action()

    def check_state_exist(self, observation):
        # 检查表中是否存在了observation状态，不存在就加入observation
        if observation not in self.q_table.index:
            self.q_table = self.q_table.append(pd.Series(
                [0] * len(self.actions),
                index=self.q_table.columns,
                name=observation
            ))

    def begin_episode(self, initial_observation):
        # 返回选择的动作
        self._current_observation = initial_observation
        self._current_action = self.choose_action()
        return self._current_action
