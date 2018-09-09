import os


def get_dir():
    return os.path.dirname(__file__)


def get_content_dir():
    content = f"{get_dir()}/content/"
    if not os.path.exists(content):
        os.mkdir(content)
    return f"{get_dir()}/content/"
