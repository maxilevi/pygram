import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='Path to the image file.')
parser.add_argument('caption', type=str, help='Caption the image should be published with.')
parser.add_argument('--use_tags', type=bool,
                    help='Append the tags in the settings.json file to the caption', default=True)
args = parser.parse_args()
