import aiohttp
import asyncio
import async_timeout
import os

from pydest.utils import check_alphanumeric


BASE_URL = 'https://www.bungie.net/Platform/Destiny2/'

class Pydest:

    def __init__(self, api_key):
        self.api_key = api_key


    async def manifest_db(self):
        """Create a Manifest database"""
        json = await self.get_destiny_manifest()

        if json['ErrorCode'] != 1:
            return None

        url = 'https://www.bungie.net' + json['Response']['mobileWorldContentPaths']['en']
        async with aiohttp.ClientSession() as session:
            await self._download_coroutine(url)


    async def _download_coroutine(self, url):
        """Download file at the given URL"""
        async with aiohttp.ClientSession() as session:
            with async_timeout.timeout(10):
                async with session.get(url) as response:
                    filename = os.path.basename(url)
                    with open(filename, 'wb') as f_handle:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            f_handle.write(chunk)
                    return await response.release()


    async def _get_request(self, url, json=True):
        """Make an async GET request and attempt to return json (dict)"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as r:
                if json:
                    return await r.json()
                else:
                    return r


    async def get_destiny_manifest(self):
        """Returns the current version of the manifest

        Returns:
            json (dict)
        """
        url = BASE_URL + 'Manifest'
        return await self._get_request(url)


    async def search_destiny_player(self, membership_type, display_name):
        """Returns a list of Destiny memberships given a full Gamertag or PSN ID

        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            display_name (str):
                The full gamertag or PSN id of the player. Spaces and case are ignored.

        Returns:
            json (dict)
        """
        check_alphanumeric(membership_type, display_name)
        url = BASE_URL + 'SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return await self._get_request(url)


    async def get_profile(self, membership_type, membership_id, components):
        """Returns Destiny Profile information for the supplied membership

        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            components (list):
                A list containing the components  to include in the response.
                (see Destiny.Responses.DestinyProfileResponse). At least one
                component is required to receive results. Can use either ints
                or strings.

        Returns:
            json (dict)
        """
        check_alphanumeric(membership_type, membership_id)
        url = BASE_URL + '{}/Profile/{}/?components={}'
        url = url.format(membership_type, membership_id, ','.join([str(i) for i in components]))
        print(url)
        return await self._get_request(url)


    async def get_character(self, membership_type, membership_id, character_id):
        """Returns character information for the supplied character

        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            character_id (int):
                ID of the character

        Returns:
            json (dict)
        """
        check_alphanumeric(membership_type, membership_id, character_id)
        url = BASE_URL + '{}/Profile/{}/Character/{}/'
        url = url.format(membership_type, membership_id, character_id)
        return await self._get_request(url)


    async def get_clan_weekly_reward_state(self, group_id):
        """Returns information on the weekly clan rewards and if the clan has earned
        them or not. Note that this will always report rewards as not redeemed.

        Args:
            group_id (int):
                A valid group ID of a clan

        Returns:
            json (dict)
        """
        check_alphanumeric(group_id)
        url = BASE_URL + 'Clan/{}/WeeklyRewardState/'
        url = url.format(group_id)
        return await self._get_request(url)


    async def get_item(self, membership_type, membership_id, item_instance_id, components):
        """Retrieve the details of an instanced Destiny Item. An instanced Destiny
        item is one with an ItemInstanceId. Non-instanced items, such as materials,
        have no useful instance-specific details and thus are not queryable here.

        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            item_instance_id (int):
                The instance ID of the item
            components (list):
                A list containing the components to include in the response
                (see Destiny.Responses.DestinyItemResponse). At least one
                component is required to receive results. Can use either ints
                or strings.

        Returns:
            json (dict)
        """
        check_alphanumeric(membership_type, membership_id, item_instance_id)
        url = BASE_URL + '{}/Profile/{}/Item/{}/?components={}'
        url = url.format(membership_type, membership_id, item_instance_id, ','.join([str(i) for i in components]))
        return await self._get_request(url)


    async def get_post_game_carnage_report(self, activity_id):
        """Gets the available post game carnage report for the activity ID

        Args:
            activity_id (int):
                The ID of the activity whose PGCR is requested

        Returns:
            json (dict)
        """
        check_alphanumeric(activity_id)
        url = BASE_URL + 'Stats/PostGameCarnageReport/{}/'
        url = url.format(activity_id)
        return await self._get_request(url)


    async def get_historical_stats_definition(self):
        """Gets historical stats definitions

        Returns:
            json (dict)
        """
        url = BASE_URL + 'Stats/Definition/'
        return await self._get_request(url)


    async def get_public_milestone_content(self, milestone_hash):
        """Gets custom localized content for the milestone of
        the given hash, if it exists.

        Returns:
            json (dict)
        """
        check_alphanumeric(milestone_hash)
        url = BASE_URL + 'Milestones/{}/Content/'
        url = url.format(milestone_hash)
        return await self._get_request(url)


    async def get_public_milestones(self):
        """Gets public information about currently available Milestones

        Returns:
            json (dict)
        """
        url = BASE_URL + 'Milestones/'
        return await self._get_request(url)
