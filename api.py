import aiohttp

class API:

    def __init__(self, api_key):
        self.api_key = api_key


    async def _get_request(self, url):
        """Make an async GET request"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with aiohttp.get(url, headers=headers) as r:
            if r.status == 200:
                return await r.json()


    async def search_destiny_player(self, membership_type, display_name):
        url = 'https://www.bungie.net/Platform/Destiny/SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return await self._get_request(url)
