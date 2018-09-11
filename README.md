# PyGram
A python bot that posts saved images to instagram on a configured schedule.

## How to schedule a post
Use the `schedule.py` tool
```
$ python schedule.py -h
usage: schedule.py [-h] [--path PATH] [--url URL] [--tags TAGS] caption

positional arguments:
  caption      Caption the image should be published with.

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  Path to the image file.
  --url URL    Url to the image file.
  --tags TAGS  Append the tags in the settings.json file to the caption.
               Separated by a comma
```
```
$ python schedule.py --path='<path-to-file>' --tags='tag1,tag2,tag3' 'A really descriptive caption'
```
## How to Setup
To run the bot you need a settings.json file defining your Instagram credentials, below are some examples.

### Example `settings.json`
```
{
  "username" : "foo",
  "password" : "bar",
  "extra_caption" : "",
  "tags" : [
    "nature",
    "forests",
    "trees"
  ]
}
```
This config will post a scheduled image every time it's executed (I suggest using `cron` for this), using the defined tags on the `foo` account with the `bar`, with no extra caption.

## license
(c) 2018 MIT License. Maxi Levi
