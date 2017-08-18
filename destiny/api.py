import aiohttp
import re

from destiny.utils import check_alphanumeric


BASE_URL = 'https://www.bungie.net/Platform/Destiny/'

class API:

    def __init__(self, api_key):
        self.api_key = api_key


    async def _get_request(self, url):
        """Make an async GET request"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with aiohttp.get(url, headers=headers) as r:
            return await r.json()


    async def search_destiny_player(self, membership_type, display_name):
        check_alphanumeric(membership_type, display_name)
        url = BASE_URL + 'SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return await self._get_request(url)


    async def get_account_summary(self, membership_type, membership_id):
        check_alphanumeric(membership_type, membership_id)
        url = BASE_URL + '{}/Account/{}/Summary/'
        url = url.format(membership_type, membership_id)
        return await self._get_request(url)
