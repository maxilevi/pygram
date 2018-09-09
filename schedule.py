import argparse
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


parser = argparse.ArgumentParser()
parser.add_argument('caption', type=str, help='Caption the image should be published with.')
parser.add_argument('--path', type=str, help='Path to the image file.')
parser.add_argument('--url', type=str, help='Url to the image file.')
parser.add_argument('--tags', type=str,
                    help='Append the tags in the settings.json file to the caption. Separated by a comma', default='')
args = parser.parse_args()
schedule(
    url=f"file:///{args.path}" if args.path is not None else args.url,
    caption=args.caption,
    tags=args.tags
)


