import urllib.request
import string
import random
import project
from os import path
import json


def get_schedule_path() -> str:
    return f"{project.get_dir()}/scheduled.json"


def load() -> dict:
    file = get_schedule_path()
    if path.exists(file):
        with open(file, 'r') as fp:
            return json.load(fp)
    else:
        return {}


def save(data: dict):
    with open(get_schedule_path(), 'w') as fp:
        json.dump(data, fp)


def random_code() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


def schedule(url: str, caption: str, tags: str):
    code = random_code()
    image_path = f"{project.get_content_dir()}/{code}"
    urllib.request.urlretrieve(url, image_path)
    saved = load()
    saved[code] = {
        'image': image_path,
        'caption': caption,
        'tags': ("".join(tags.split())).split(',')  # Remove all whitespace and then separate by ,
    }
    save(saved)
