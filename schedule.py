import argparse
import scheduler


parser = argparse.ArgumentParser()
parser.add_argument('caption', type=str, help='Caption the image should be published with.')
parser.add_argument('--path', type=str, help='Path to the image file.')
parser.add_argument('--url', type=str, help='Url to the image file.')
parser.add_argument('--tags', type=str, help='Append the tags in the settings.json file to the caption. Separated by a comma', default='')
args = parser.parse_args()
scheduler.schedule(
    url=f"file:///{args.path}" if args.path is not None else args.url,
    caption=args.caption,
    tags=args.tags
)


