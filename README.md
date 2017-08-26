# pydest
Pydest is an asynchronous Destiny 2 API wrapper written in Python.

My initial goal with this project is to provide a basic wrapper around all of
the provided API calls, and do nothing more than do some simple argument checks
and making the async request. This is all fine and well, but in the future I'd
like to build up several helper methods that make the whole process even easier.

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

All GET endpoints that are not in a preview are supported. I will add support for
the other GET endpoints when they leave the preview state. I also plan to add
the POST endpoints when I have a better understanding of how they work.

## Installation
[TODO]

## Usage
This example illustrates the basic work flow for pydest (I'm assuming you're
already running an event loop here)
```
import aiohttp
import pydest

destiny = pydest.api('your-api-key')
json_response = await destiny.search_destiny_player(1, 'jimmy')
```
All of the API calls can be found in [api.py](./pydest/api.py), and I've added
fairly descriptive docstring to each function to explain how to use them. I've
used the exact same argument names as in the official documentation, though
I'm using the underscore naming convention instead of camel case.
