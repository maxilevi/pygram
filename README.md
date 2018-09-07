# PyGram
A python bot that posts saved images to instagram on a configured schedule.

## How to schedule a post
Use the `schedule.py` tool
```
$ python schedule.py -h
usage: schedule.py [-h] [--use_tags USE_TAGS] path caption

positional arguments:
  path                 Path to the image file.
  caption              Caption the image should be published with.

optional arguments:
  -h, --help           show this help message and exit
  --use_tags USE_TAGS  Append the tags in the settings.json file to the
                       caption
```
## How to Setup
To run the bot you need a settings.json file defining your Instagram credentials, below are some examples.

### Example `settings.json`
```
{
  "username" : "user123",
  "password" : "pass123",
  "frequency" : {
    "minute" : "30",
    "hour" : "12",
    "day"  : "*",
  },
  "tags" : [
    "nature",
    "forests",
    "trees"
  ]
}
```
This config will post a scheduled image every day at 12:30 PM, using the defined tags on the 'user123' account with the 'pass123'.

## license
(c) 2018 MIT License. Maxi Levi
