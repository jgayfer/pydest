# Pydest

Pydest is an asynchronous API wrapper for Destiny 2 written in Python. The goal of the project is to fully support the Destiny 2 API while abstracting the details of formulating and making the request away from the user.

Here are some examples of Pydest in action (assuming this code is running in an event loop):

```python
import pydest

destiny = pydest.Pydest('your-api-key')
json = await destiny.api.search_destiny_player(1, 'slayer117')
await destiny.close()
```

Pydest also has full support for easily decoding hash values from the Destiny 2 manifest.

```python
import pydest

destiny = pydest.Pydest('your-api-key')
json = await pydest.decode_hash(80726883, 'DestinyActivityDefinition')
await destiny.close()
```

For some working examples of Pydest, refer to the [examples](./examples) folder.

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
$ pip install pydest
```
To verify that Pydest has installed correctly, open up the Python interpreter and run the command `import pydest`. If the interpreter doesn't make a fuss, then Pydest has installed successfully.

## Documentation

### Pydest

>**class pydest.Pydest(api_key,loop=None)**

The base object for Pydest contains various helper functions, such as looking up items in the Destiny 2 manifest. This object must be initialized before Pydest can be used.

**Parameters**

- `api_key` - Bungie.net API key. A key can be obtained from [Bungie.net/en/application](https://www.bungie.net/en/application)
- `loop` [optional] - The event loop to use for asynchronous operations. Defaults to `None`, in which case the default event loop is used via `asyncio.get_event_loop()`.

---

> api

A reference to an [API](/pydest/api.py) object. This is used to call Destiny 2 API calls directly (see below).

---

> close()

This function is a coroutine.

Closes the Pydest client session. This should be called when the Pydest object is no longer needed. If this isn't called, a warning message will be displayed, but Pydest will stil function.

---

> decode_hash(hash_id, definition, language='en')

This function is a coroutine.

Get the corresponding static info for an item given it's hash value. The first time this is called, it will download and extract the latest version of the Destiny 2 manifest to the current directory if it isn't already there. It's recommended to keep this file around so that it isn't downloaded each time an item needs to be decoded.

Aside from the very first time this function is called (when the manifest is downloaded), this function is fast. There are no network requests made; the only action is querying a database. So don't worry about calling this lots!

**Parameters**
- `hash_id` - The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
- `definition` - The type of entity to be decoded. In the [official documentation](https://bungie-net.github.io/multi/index.html), these entities are proceeded by a blue 'Manifest' tag (eg. *DestinyClassDefinition*).
- `language` [optional] - The desired language of the response, given as a string. The following languages are supported (and should be given as shown): en, fr, es, de, it, ja, pt-br, es-mx, ru, pl, zn-cht, ko, zh-chs. If no language is given, English will be used.

**Returns**: Python dictionary containing static information that the given hash and definition represent in JSON.

**Raises**: *PydestException* if entry cannot be found

---

> update_manifest(language='en')

This function is a coroutine.

Updates the manifest corresponding to the language given. If no language is given, the default is English. This function is designed to be used for a program that is running for extended periods of time where the manifest may need to be updated. Usually the manifest is only updated the first time that `decode_hash()` is called. But as the manifest will likely change over time, this function will help keep the manifest current.

**Parameters**
- `language` [optional] - The desired language of the response, given as a string. The following languages are supported (and should be given as shown): en, fr, es, de, it, ja, pt-br, es-mx, ru, pl, zn-cht, ko, zh-chz. If no language is given, English will be used.

### API

> **pydest.API(api_key, session)**

The API class contains all of the supported Destiny 2 API calls. The functions contained in this class don't perform any magic; they simply make the API call and return the JSON sent from the Bungie servers.

**Parameters**

- `api_key` - Bungie.net API key. A key can be obtained from [Bungie.net/en/application](https://www.bungie.net/en/application)
- `session` - An `aiohttp` client session

---

> get_bungie_net_user_by_id(bungie_id)

This function is a coroutine.

Loads a bungienet user by membership id.

**Parameters**
- `bungie_id` - The requested Bungie.net membership id

**Response**:
[User.GeneralUser](https://bungie-net.github.io/multi/schema_User-GeneralUser.html#schema_User-GeneralUser)

---

> get_membership_data_by_id(bungie_id, membership_type=-1)

This function is a coroutine.

Returns a list of accounts associated with the supplied membership ID and membership type. This will
include all linked accounts (even when hidden) if supplied credentials permit it.

**Parameters**
- `bungie_id` - The requested Bungie.net membership id
- `membership_type` [optional] - Type of the supplied membership ID. If not provided, data will be
returned for all applicable platforms.

**Response**:
[User.UserMembershipData](https://bungie-net.github.io/multi/schema_User-UserMembershipData.html#schema_User-UserMembershipData)

---

> get_destiny_manifest()

This function is a coroutine.

Get the current version of the manifest. This api call shouldn't be needed much, as `Pydest.decode_hash()` already takes care of most manifest use cases.

**Response**: See [Destiny2.GetDestinyManifest](https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyManifest.html#operation_get_Destiny2-GetDestinyManifest#Response)

---

> get_destiny_entity_definition(entity_type, hash_identifier)

This function is a coroutine.

Returns the static definition of an entity of the given Type and hash identifier

**Parameters**
- `entity_type` - The type of entity - ex. 'DestinyInventoryItemDefinition'
- `hash_identifier` - The hash identifier for the specific Entity you want returned.

**Response**: 
See [Destiny2.GetDestinyEntityDefinition](https://bungie-net.github.io/multi/schema_Destiny-Definitions-DestinyDefinition.html#schema_Destiny-Definitions-DestinyDefinition)

---

> search_destiny_entities(entity_type, search_term, page=0)

This function is a coroutine.

Gets a page list of Destiny items.

**Parameters**
- `entity_type` - The type of entity - ex. 'DestinyInventoryItemDefinition'
- `search_term` - The term to search for
- `page` [optional] - Page number to return

**Response**:
[Destiny2.DestinyEntitySearchResult](https://bungie-net.github.io/multi/schema_Destiny-Definitions-DestinyEntitySearchResult.html#schema_Destiny-Definitions-DestinyEntitySearchResult)

---

> search_destiny_player(membership_type, display_name)

This function is a coroutine.

Returns a list of Destiny memberships given a full Gamertag or PSN ID.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `display_name` - The full gamertag or PSN id of the player. Spaces and case is ignored.

**Response**: See [Destiny2.SearchDestinyPlayer](https://bungie-net.github.io/multi/operation_get_Destiny2-SearchDestinyPlayer.html#operation_get_Destiny2-SearchDestinyPlayer)

---

> get_profile(membership_type, membership_id, components)

This function is a coroutine.

Returns Destiny Profile information for the supplied membership.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` - The full gamertag or PSN id of the player. Spaces and case are ignored.
- `components` - A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetProfile](https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html#operation_get_Destiny2-GetProfile)

---

> get_character(membership_type, membership_id, character_id, components)

This function is a coroutine.

Returns character information for the supplied character.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` - The full gamertag or PSN id of the player. Spaces and case are ignored.
- `character_id` - ID of the character.
- `components` - A Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetCharacter](https://bungie-net.github.io/multi/operation_get_Destiny2-GetCharacter.html#operation_get_Destiny2-GetCharacter)

---

> get_clan_weekly_reward_state(group_id)

This function is a coroutine.

Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

**Parameters**
- `group_id` - A valid clan group id.

**Response**: See [Destiny2.GetClanWeeklyRewardState](https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanWeeklyRewardState.html#operation_get_Destiny2-GetClanWeeklyRewardState)

---

> get_item(membership_type, membership_id, item_instance_id, components)

This function is a coroutine.

Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` - The full gamertag or PSN id of the player. Spaces and case are ignored.
- `item_instance_id` - The Instance ID of the destiny item.
- `components` - A  Python list of [Destiny.DestinyComponentType](https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html#schema_Destiny-DestinyComponentType) (as strings or numeric values) to include in the response.

**Response**: See [Destiny2.GetItem](https://bungie-net.github.io/multi/operation_get_Destiny2-GetItem.html#operation_get_Destiny2-GetItem)

---

> get_post_game_carnage_report(activity_id)

This function is a coroutine.

Gets the available post game carnage report for the activity ID.

**Parameters**
- `activity_id` - The ID of the activity whose PGCR is requested.

**Response**: See [Destiny2.GetPostGameCarnageReport](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPostGameCarnageReport.html#operation_get_Destiny2-GetPostGameCarnageReport)

---

> get_historical_stats_definition()

This function is a coroutine.

Gets historical stats definitions.

**Response**: See [Destiny2.GetHistoricalStatsDefinition](https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStatsDefinition.html#operation_get_Destiny2-GetHistoricalStatsDefinition)

---

> get_historical_stats(membership_type, membership_id, character_id=0, groups=[], modes=[])

This function is a coroutine.

Gets historical stats for indicated character.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` - The full gamertag or PSN id of the player. Spaces and case are ignored.
- `character_id [optional]` - ID of the character. If not provided, stats for all characters will be returned.
- `groups` - A list containing the groups of stats to include in the response (see [Destiny.HistoricalStats.Definitions.DestinyStatsGroupType](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-Definitions-DestinyStatsGroupType.html#schema_Destiny-HistoricalStats-Definitions-DestinyStatsGroupType)).
- `modes` - A list containing the game modes to include in the response (see [Destiny.HistoricalStats.Definitions.DestinyActivityModeType](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-Definitions-DestinyActivityModeType.html#schema_Destiny-HistoricalStats-Definitions-DestinyActivityModeType)).

**Response**
See [Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-DestinyHistoricalStatsByPeriod.html#schema_Destiny-HistoricalStats-DestinyHistoricalStatsByPeriod)

---

> get_historical_stats_for_account(membership_type, membership_id, groups=[])

This function is a coroutine.

Gets aggregate historical stats organized around each character for a given account.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` - The full gamertag or PSN id of the player. Spaces and case are ignored.
- `groups` - A list containing the groups of stats to include in the response (see [Destiny.HistoricalStats.Definitions.DestinyStatsGroupType](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-Definitions-DestinyStatsGroupType.html#schema_Destiny-HistoricalStats-Definitions-DestinyStatsGroupType)).

**Response**
See [Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-DestinyHistoricalStatsAccountResult.html#schema_Destiny-HistoricalStats-DestinyHistoricalStatsAccountResult)

---

> get_public_milestone_content(milestone_hash)

This function is a coroutine.

Gets custom localized content for the milestone of the given hash, if it exists.

**Parameters**
- `milestone_hash` - The identifier for the milestone to be returned.

**Response**: See [Destiny2.GetPublicMilestoneContent](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestoneContent.html#operation_get_Destiny2-GetPublicMilestoneContent)

---

> get_public_milestones()

This function is a coroutine.

Gets public information about currently available Milestones.

**Response**: See [Destiny2.GetPublicMilestones](https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestones.html#operation_get_Destiny2-GetPublicMilestones)

---

> get_group_for_member()

This function is a coroutine.

Gets information about the clan of a member.

**Response**: See [GroupV2.GetGroupsForMember](https://bungie-net.github.io/multi/operation_get_GroupV2-GetGroupsForMember.html#operation_get_GroupV2-GetGroupsForMember)

---

> get_members_of_group()

This function is a coroutine.

Get the list of members and its related information in a given group.

**Parameters**
- `group_id` - The ID of the group.

**Response**: See [GroupV2.GetMembersOfGroup](https://bungie-net.github.io/multi/operation_get_GroupV2-GetMembersOfGroup.html#operation_get_GroupV2-GetMembersOfGroup)

---

> get_weekly_milestones()

This function is a coroutine.

Gets information about milestones for a clan

**Response**: See [Destiny2.GetClanWeeklyRewardState](https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanWeeklyRewardState.html#operation_get_Destiny2-GetClanWeeklyRewardState)

---

> get_weekly_milestone_definition()

This function is a coroutine.

This function retreives additional information for a milestone from the destiny2 Manifest.

**Response**: See [Destiny.Definitions.Milestones.DestinyMilestoneDefinition](https://bungie-net.github.io/multi/schema_Destiny-Definitions-Milestones-DestinyMilestoneDefinition.html#schema_Destiny-Definitions-Milestones-DestinyMilestoneDefinition)

---


> get_activity_history(membership_type, membership_id, character_id, count=1, mode=None, page=0)

This function is a coroutine.

Gets activity history stats for indicated character.

**Parameters**
- `membership_type` - A valid non-BungieNet membership type, or All. See [BungieMembershipType](https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType)
- `membership_id` - The full gamertag or PSN id of the player. Spaces and case are ignored.
- `character_id` - ID of the character.
- `count` - Number of rows to return.
- `mode` - The game mode to include in the response (see [Destiny.HistoricalStats.Definitions.DestinyActivityModeType](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-Definitions-DestinyActivityModeType.html#schema_Destiny-HistoricalStats-Definitions-DestinyActivityModeType)).
- `page` - Page number to return, starting with 0.

**Response**
See [Destiny.HistoricalStats.DestinyActivityHistoryResults](https://bungie-net.github.io/multi/schema_Destiny-HistoricalStats-DestinyActivityHistoryResults.html#schema_Destiny-HistoricalStats-DestinyActivityHistoryResults)

---

For additional information on how the API endpoints function, refer to the [official documentation](https://bungie-net.github.io/multi/index.html).

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
