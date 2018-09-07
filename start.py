import json
from worker import Grammer
from os import path


def load_config(config_path: str) -> dict:
    if not path.exists(config_path):
        raise ValueError('Config does not exist, please create a settings.json file.')
    with open(config_path, 'r') as fp:
        return json.load(fp)


config = load_config(path.dirname(__file__) + '/settings.json')
grammer = Grammer(config)
grammer.start()
