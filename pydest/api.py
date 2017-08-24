import aiohttp
import re

from pydest.utils import check_alphanumeric


BASE_URL = 'https://www.bungie.net/Platform/Destiny2/'

class API:

    def __init__(self, api_key):
        self.api_key = api_key


    async def _get_request(self, url):
        """Make an async GET request"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url, headers=headers) as r:
                return await r.json()


    async def search_destiny_player(self, membership_type, display_name):
        """Returns a list of Destiny memberships given a full Gamertag or PSN ID"""
        check_alphanumeric(membership_type, display_name)
        url = BASE_URL + 'SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return await self._get_request(url)


    async def get_profile(self, membership_type, membership_id):
        """Returns Destiny Profile information for the supplied membership"""
        check_alphanumeric(membership_type, membership_id)
        url = BASE_URL + '/{}/Profile/{}/'
        url = url.format(membership_type, membership_id)
        return await self._get_request(url)


    async def get_character(self, membership_type, membership_id, character_id):
        """Returns character information for the supplied character"""
        check_alphanumeric(membership_type, membership_id, character_id)
        url = BASE_URL + '{}/Profile/{}/Character/{}/'
        url = url.format(membership_type, membership_id, character_id)
        return await self._get_request(url)


    async def get_clan_weekly_reward_state(self, group_id):
        """Returns information on the weekly clan rewards and if
           the clan has earned them or not."""
        check_alphanumeric(group_id)
        url = BASE_URL + 'Clan/{}/WeeklyRewardState/'
        url = url.format(group_id)
        return await self._get_request(url)


    async def get_historical_stats_definition(self):
        """Gets historical stats definitions"""
        url = BASE_URL + 'Stats/Definition/'
        return await self._get_request(url)
