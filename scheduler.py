import urllib.request
import string
import random
import project
from os import path
import json
from PIL import Image


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
    image_path = f"{project.get_content_dir()}/{code}.jpg"
    _, ext = path.splitext(url)
    retrieve_as_jpg(url, image_path, ext)
    fix_aspect_ratio(image_path)
    saved = load()
    saved[code] = {
        'image': image_path,
        'caption': caption,
        'tags': ("".join(tags.split())).split(',')  # Remove all whitespace and then separate by ,
    }
    save(saved)
    print(f"'{url}' has been scheduled succesfully.")


def retrieve_as_jpg(url: str, image_path: str, ext: str):
    tmp_path = f"{image_path}{ext}"
    urllib.request.urlretrieve(url, tmp_path)
    im = Image.open(tmp_path)
    if not im.mode == 'RGB':
        im = im.convert('RGB')
    im.save(image_path, quality=95)


# https://stackoverflow.com/questions/4744372/reducing-the-width-height-of-an-image-to-fit-a-given-aspect-ratio-how-python

def fix_aspect_ratio(image_path: str):
    image = Image.open(image_path)
    width = image.size[0]
    height = image.size[1]

    aspect = width / float(height)

    ideal_aspect = 1.90  # Instagram's minimum aspect ratio https://help.instagram.com/1469029763400082

    if aspect > ideal_aspect:
        # Then crop the left and right edges:
        new_width = int(ideal_aspect * height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
    else:
        # ... crop the top and bottom:
        new_height = int(width / ideal_aspect)
        offset = (height - new_height) / 2
        resize = (0, offset, width, height - offset)

    cropped = image.crop(resize)
    cropped.save(image_path)
