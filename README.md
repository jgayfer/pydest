# Pydest

Pydest is an asynchronous API wrapper for Destiny 2 written in Python. The goal of the project is fully support the Destiny 2 API while abstracting the details of formulating and making the request away from the user.

Here are some examples of Pydest in action (assuming this code is running in an event loop):

```
import pydest

destiny = pydest.Pydest('your-api-key')
json = await destiny.api.search_destiny_player(1, 'slayer117')
```

Pydest also has full support for easily decoding hash values from the Destiny 2 manifest.

```
import pydest

destiny = pydest.Pydest('your-api-key')
json = await pydest.decode_hash(-2143553567, 'DestinyActivityDefinition')
```

For a complete working example of Pydest, refer to the [examples](./examples) folder.

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

## Documentation

#### `Pydest(api_key)`

The base object for Pydest contains various helper functions, such as looking up items in the Destiny 2 manifest.

**Parameters**
- `api_key` Bungie.net API key. Can be obtained from [Bungie.net](https://www.bungie.net/en/application)

**Returns**: `Pydest object`

---

#### `Pydest.close()`
Closes the client session. If this isn't called, a warning message will be displayed.

---

#### `Pydest.decode_hash(hash_id, definition)`
*Coroutine*

Get the corresponding static info for an item given it's hash value

**Parameters**
- `hash_id` The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
- `definition` The type of entity to be decoded. In the [official documentation](https://bungie-net.github.io/multi/index.html), these entities are proceeded by a blue 'Manifest' tag (eg. *DestinyClassDefinition*).

**Returns**: Python dictionary containing static information that the given hash and definition represent.

**Raises**: *PydestException* if entry cannot be found

---

#### `Pydest.api.get_destiny_manifest()`
*Coroutine*

Get the current version of the manifest. This api call shouldn't be needed as `Pydest.decode_hash()` already (partially) implements it.

**Response**: See [Destiny2.GetDestinyManifest](https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyManifest.html#operation_get_Destiny2-GetDestinyManifest#Response)

---

#### `Pydest.api.search_destiny_player(membership_type, display_name)`
*Coroutine*

Returns a list of Destiny memberships given a full Gamertag or PSN ID.

**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `display_name` The full gamertag or PSN id of the player. Spaces and case is ignored.

**Response**: See [Destiny2.SearchDestinyPlayer](https://bungie-net.github.io/multi/operation_get_Destiny2-SearchDestinyPlayer.html#operation_get_Destiny2-SearchDestinyPlayer)

---

#### `Pydest.api.get_profile(membership_type, membership_id, components)`
*Coroutine*

Returns Destiny Profile information for the supplied membership.

**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` The full gamertag or PSN id of the player. Spaces and case are ignored.
- `components` A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetProfile](https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html#operation_get_Destiny2-GetProfile)

---

#### `Pydest.api.get_character(membership_type, membership_id, character_id, components)`
*Coroutine*

Returns character information for the supplied character.

**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` The full gamertag or PSN id of the player. Spaces and case are ignored.
- `character_id` ID of the character.
- `components` A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetCharacter](https://bungie-net.github.io/multi/operation_get_Destiny2-GetCharacter.html#operation_get_Destiny2-GetCharacter)

---

#### `Pydest.api.get_clan_weekly_reward_state(group_id)`
*Coroutine*

Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

**Parameters**
- `group_id` A valid clan group id.

**Response**: See [Destiny2.GetClanWeeklyRewardState](https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanWeeklyRewardState.html#operation_get_Destiny2-GetClanWeeklyRewardState)

---

#### `Pydest.api.get_item(membership_type, membership_id, item_instance_id, components)`
*Coroutine*

Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

**Parameters**
- `membership_type` A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` The full gamertag or PSN id of the player. Spaces and case are ignored.
- `item_instance_id` The Instance ID of the destiny item.
- `components` A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetItem](https://bungie-net.github.io/multi/operation_get_Destiny2-GetItem.html#operation_get_Destiny2-GetItem)

---

#### `Pydest.api.get_post_game_carnage_report(activity_id)`
*Coroutine*

Gets the available post game carnage report for the activity ID.

**Parameters**
- `activity_id`The ID of the activity whose PGCR is requested.

**Response**: See [Destiny2.GetPostGameCarnageReport](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPostGameCarnageReport.html#operation_get_Destiny2-GetPostGameCarnageReport)

---

#### `Pydest.api.get_historical_stats_definition()`
*Coroutine*

Gets historical stats definitions.

**Response**: See [Destiny2.GetHistoricalStatsDefinition](https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStatsDefinition.html#operation_get_Destiny2-GetHistoricalStatsDefinition)

---

#### `Pydest.api.get_public_milestone_content(milestone_hash)`
*Coroutine*

Gets custom localized content for the milestone of the given hash, if it exists.

**Parameters**
- `milestone_hash` The identifier for the milestone to be returned.

**Response**: See [Destiny2.GetPublicMilestoneContent](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestoneContent.html#operation_get_Destiny2-GetPublicMilestoneContent)

---

#### `Pydest.api.get_public_milestones()`
*Coroutine*

Gets public information about currently available Milestones.

**Response**: See [Destiny2.GetPublicMilestones](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestones.html#operation_get_Destiny2-GetPublicMilestones)

---

For additional information on how the API endpoints function, refer to the [official documentation](https://bungie-net.github.io/multi/index.html).

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
