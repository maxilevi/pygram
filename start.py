import json
from worker import Instagrammer
from os import path
import project


def load_config(config_path: str) -> dict:
    if not path.exists(config_path):
        raise ValueError('Config does not exist, please create a settings.json file.')
    with open(config_path, 'r') as fp:
        return json.load(fp)


config = load_config(f"{project.get_dir()}/settings.json")
instagrammer = Instagrammer(config)
instagrammer.start()
