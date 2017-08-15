import aiohttp
import re

class API:

    def __init__(self, api_key):
        self.api_key = api_key


    async def _get_request(self, url):
        """Make an async GET request"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with aiohttp.get(url, headers=headers) as r:
            return await r.json()


    def check_args(self, *args):
        """Check API arguments are alphanumeric"""
        for arg in args:
            valid = re.match('^[\w-]+$', str(arg))
            if not valid:
                raise ValueError("arguments must consist of alphanumeric characters only")


    async def search_destiny_player(self, membership_type, display_name):
        self.check_args(membership_type, display_name)
        url = 'https://www.bungie.net/Platform/Destiny/SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return await self._get_request(url)


    async def get_account_summary(self, membership_type, membership_id):
        self.check_args(membership_type, membership_id)
        url = 'https://www.bungie.net/Platform/Destiny/{}/Account/{}/Summary/'
        url = url.format(membership_type, membership_id)
        return await self._get_request(url)
