# Pydest

Pydest is an asynchronous API wrapper for Destiny 2 written in Python. The goal of the project is fully support the Destiny 2 API while abstracting the details of formulating and making the request away from the user.

Here's a quick example of Pydest in action (assuming this code is running in an event loop):

```
import aiohttp
import pydest

with pydest.API('your-api-key') as destiny:
    response = await destiny.search_destiny_player(1, 'slayer117')
```

That's it!

Currently all GET endpoints that are not in a preview state are supported by Pydest. The other GET endpoints will be added when they leave the preview state. Support for the POST endpoints will be added at a later date.

## Prerequisites
The following dependencies are required to use Pydest. Note that `pytest` and any related plugins are only required if the user wishes to run the unit and integration tests.
- Python 3.5+
- `aiohttp` library
- `pytest` library
- `pytest-asyncio` (pytest plugin)

Usually `pip` will handle the installation of these.

## Installation
```
$ git clone https://github.com/jgayfer/pydest
$ cd pydest
$ python3 -m pip install -U .
```
To verify that Pydest has installed correctly, open up the Python interpreter and run the command `import pydest`. If the interpreter doesn't make a fuss, then Pydest has installed successfully.

## API Endpoints

All of the functions below are *couroutines*. In other words, they must be awaited!

---

#### `pydest.API.get_destiny_manifest()`
Get the current version of the manifest.

**Response**: See [Destiny2.GetDestinyManifest](https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyManifest.html#operation_get_Destiny2-GetDestinyManifest#Response)

---

#### `pydest.API.search_destiny_player(membership_type, display_name)`
Returns a list of Destiny memberships given a full Gamertag or PSN ID.

######**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `display_name` The full gamertag or PSN id of the player. Spaces and case is ignored.

**Response**: See [Destiny2.SearchDestinyPlayer](https://bungie-net.github.io/multi/operation_get_Destiny2-SearchDestinyPlayer.html#operation_get_Destiny2-SearchDestinyPlayer)

---

#### `pydest.API.get_profile(membership_type, membership_id, components)`
Returns Destiny Profile information for the supplied membership.

######**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` The full gamertag or PSN id of the player. Spaces and case are ignored.
- `components` A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetProfile](https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html#operation_get_Destiny2-GetProfile)

---

#### `pydest.API.get_character(membership_type, membership_id, character_id, components)`
Returns character information for the supplied character.

######**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` The full gamertag or PSN id of the player. Spaces and case are ignored.
- `character_id` ID of the character.
- `components` A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetCharacter](https://bungie-net.github.io/multi/operation_get_Destiny2-GetCharacter.html#operation_get_Destiny2-GetCharacter)

---

#### `pydest.API.get_clan_weekly_reward_state(group_id)`
Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

######**Parameters**
- `group_id` A valid clan group id.

**Response**: See [Destiny2.GetClanWeeklyRewardState](https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanWeeklyRewardState.html#operation_get_Destiny2-GetClanWeeklyRewardState)

---

#### `pydest.API.get_item(membership_type, membership_id, item_instance_id, components)`
Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

######**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` The full gamertag or PSN id of the player. Spaces and case are ignored.
- `item_instance_id` The Instance ID of the destiny item.
- `components` A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetItem](https://bungie-net.github.io/multi/operation_get_Destiny2-GetItem.html#operation_get_Destiny2-GetItem)

---

#### `pydest.API.get_post_game_carnage_report(activity_id)`
Gets the available post game carnage report for the activity ID.

######**Parameters**
- `activity_id`The ID of the activity whose PGCR is requested.

**Response**: See [Destiny2.GetPostGameCarnageReport](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPostGameCarnageReport.html#operation_get_Destiny2-GetPostGameCarnageReport)

---

#### `pydest.API.get_historical_stats_definition()`
Gets historical stats definitions.

**Response**: See [Destiny2.GetHistoricalStatsDefinition](https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStatsDefinition.html#operation_get_Destiny2-GetHistoricalStatsDefinition)

---

#### `pydest.API.get_public_milestone_content(milestone_hash)`
Gets custom localized content for the milestone of the given hash, if it exists.

**Response**: See [Destiny2.GetPublicMilestoneContent](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestoneContent.html#operation_get_Destiny2-GetPublicMilestoneContent)

---

#### `pydest.API.get_public_milestones()`
Gets public information about currently available Milestones.

**Response**: See [Destiny2.GetPublicMilestones](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestones.html#operation_get_Destiny2-GetPublicMilestones)

---

## Running Tests

There is a series of integration tests that can be run to verify that Pydest is working as intended. These tests will hit all supported Destiny 2 endpoints with well formed requests, and verify that a valid response is received. The main reason reason that these tests would fail, is if the Bungie.net servers are down, or the endpoints themselves have changed.

Before these tests can be run, you'll need to create a `credentials.json` file in the root directory of this project. This file will contain your api key.
```
{
  "api-key": "your-api-key"
}
```
The integration tests can be run from the root directory with the following command:
```
pytest -k 'integration'
```
Unit tests can be run from the root directory with:
```
pytest -k 'not integration'
```
