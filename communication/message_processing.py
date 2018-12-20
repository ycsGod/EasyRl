# -*- coding: utf-8 -*-

import requests
import json
from message import Message


class MSGProcessing(object):
    CREATE_ENV_URL = "http://127.0.0.1:5000/create_env"
    RESET_ENV_URL = "http://127.0.0.1:5000/reset_env"
    ENV_STEP_URL = "http://127.0.0.1:5000/step_env"
    ENV_STOP_URL = "http://127.0.0.1:5000/stop_env"
    __url_list = [CREATE_ENV_URL, RESET_ENV_URL, ENV_STEP_URL, ENV_STOP_URL]

    @staticmethod
    def send(url, msg):
        # 应该要考虑url不对的情况

        if url in MSGProcessing.__url_list:
            return MSGProcessing.deserialization(requests.post(url, MSGProcessing.serialization(msg)).text)
        else:
            raise ValueError("url is not correct!")

    @staticmethod
    def serialization(msg):
        return json.dumps(msg, default=MSGProcessing.message2dict)

    @staticmethod
    def deserialization(json_data):
        return json.loads(json_data, object_hook=MSGProcessing.dict2message)

    @staticmethod
    def message2dict(msg):
        return {
            "env_id": msg.env_id,
            "game_name": msg.game_name,
            "is_reset": msg.is_reset,
            "action_space": msg.action_space,
            "action": msg.action,
            "initial_observation": msg.initial_observation,
            "observation": msg.observation,
            "num_features": msg.num_features,
            "reward": msg.reward,
            "is_terminal": msg.is_terminal
        }

    @staticmethod
    def dict2message(json_data):
        return Message(
            json_data['env_id'],
            json_data['game_name'],
            json_data['is_reset'],
            json_data['action_space'],
            json_data['action'],
            json_data['initial_observation'],
            json_data['observation'],
            json_data['num_features'],
            json_data['reward'],
            json_data['is_terminal']
        )

