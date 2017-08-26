# pydest
Pydest is an asynchronous Destiny 2 API wrapper written in Python.

## Supported Endpoints
For a description of each endpoint, refer to the [official documentation](https://bungie-net.github.io/multi/index.html)
- GET: Destiny2.GetDestinyManifest
- GET: Destiny2.SearchDestinyPlayer
- GET: Destiny2.GetProfile
- GET: Destiny2.GetCharacter
- GET: Destiny2.GetClanWeeklyRewardState
- GET: Destiny2.GetItem
- GET: Destiny2.GetPostGameCarnageReport
- GET: Destiny2.GetHistoricalStatsDefinition
- GET: Destiny2.GetPublicMilestoneContent
- GET: Destiny2.GetPublicMilestones

All GET endpoints that are not in a preview state are supported. I will add support for
the other GET endpoints when they leave the preview state. I also plan to add
the POST endpoints when I have a better understanding of how they work.

## Installation
```
$ git clone https://github.com/jgayfer/pydest
$ cd pydest
$ python3 -m pip install -U .
```

## Usage
This example illustrates the basic work flow for pydest (I'm assuming you're
already running an event loop here)
```
import aiohttp
import pydest

with pydest.API('your-api-key') as destiny:
      json = await destiny.search_destiny_player(1, 'AsalX')
      # Do stuff, or make additional api calls
```
All of the API calls can be found in [api.py](./pydest/api.py). I've added
fairly descriptive docstring to each function to explain how to use them. I've
also used the exact same argument names as in the official documentation,
though I'm using the underscore naming convention instead of camel case.
