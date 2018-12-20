# -*- coding: utf-8 -*-

import json


class Config(object):

    def __init__(self):
        self._create_env_url = None
        self._reset_env_url = None
        self._env_step_url = None
        self._env_stop_url = None
        self._env_render_url = None
        self._url_list = []
        self.read_config()

    def read_config(self, config_path="/home/cs/PycharmProjects/EasyRL/communication/server_config.json"):
        with open(config_path, 'r') as configs:
            data = json.load(configs)
            self._create_env_url = data['create_env_url']
            self._reset_env_url = data['env_reset_url']
            self._env_step_url = data['env_step_url']
            self._env_stop_url = data['env_stop_url']
            self._env_render_url = data['env_render_url']

            self._url_list.append(self._create_env_url)
            self._url_list.append(self._reset_env_url)
            self._url_list.append(self._env_step_url)
            self._url_list.append(self._env_stop_url)
            self._url_list.append(self._env_render_url)

    @property
    def create_env_url(self):
        return self._create_env_url

    @property
    def reset_env_url(self):
        return self._reset_env_url

    @property
    def env_step_url(self):
        return self._env_step_url

    @property
    def env_stop_url(self):
        return self._env_stop_url

    @property
    def env_render_url(self):
        return self._env_render_url

