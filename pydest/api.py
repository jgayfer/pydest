import aiohttp
import re

from pydest.utils import check_alphanumeric


BASE_URL = 'https://www.bungie.net/Platform/Destiny2/'

class API:
    """This module contains async requests for the Destiny 2 API.
    There is some documentation provided here as to how to use
    these functions, but you will likely need to refer to the
    official API documentation as well. The documentation can be
    found at https://bungie-net.github.io/multi/index.html
    """

    def __init__(self, api_key):
        self.api_key = api_key


    def __enter__(self):
        self.session = aiohttp.ClientSession()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()


    async def _get_request(self, url):
        """Make an async GET request and attempt to return json (dict)"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with self.session.get(url, headers=headers) as r:
            return await r.json()


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
            components (tuple):
                A tuple containing a list of components (DestinyComponentType)
                to include in the response. At least one component is required
                to receive results.

        Returns:
            json (dict)
        """
        check_alphanumeric(membership_type, membership_id)
        url = BASE_URL + '{}/Profile/{}/?components={}'
        url = url.format(membership_type, membership_id, ','.join(components))
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


    async def get_item(self, membership_type, membership_id, item_instance_id):
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

        Returns:
            json (dict)
        """
        check_alphanumeric(membership_type, membership_id, item_instance_id)
        url = BASE_URL + '{}/Profile/{}/Item/{}'
        url = url.format(membership_type, membership_id, item_instance_id)
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
