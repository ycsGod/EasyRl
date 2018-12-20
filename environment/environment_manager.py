# -*- coding: utf-8 -*-

import uuid


class EnvManager(object):
    def __init__(self):
        self._ID_list = set()
        self._env_dict = {}

    '''
    为环境创建唯一的ID
    '''
    def add_env(self, env):
        while True:
            env_id = str(uuid.uuid4())
            if env_id not in self._ID_list:
                self._ID_list.add(env_id)
                self._env_dict[env_id] = env
                print "Successfully add env(env_id={})".format(env_id)
                return env_id

    '''
    当环境终止,删除对应的ID
    '''
    def delete_env(self, env_id):
        if env_id in self._ID_list:
            self._ID_list.remove(env_id)
            del self._env_dict[env_id]
            print "Successfully delete env(env_id={})".format(env_id)

    @property
    def env_dict(self):
        return self._env_dict

    @env_dict.setter
    def env_dict(self, env_dict):
        self._env_dict = env_dict
