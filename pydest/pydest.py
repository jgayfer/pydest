import aiohttp
import asyncio
import async_timeout
import os

from pydest.utils import check_alphanumeric
from pydest.api import API


BASE_URL = 'https://www.bungie.net/Platform/Destiny2/'

class Pydest:

    def __init__(self, api_key):
        self.api = API(api_key)


    def close(self):
        self.api.close_session()


    async def manifest_db(self):
        """Create a Manifest database"""
        json = await self.api.get_destiny_manifest()

        if json['ErrorCode'] != 1:
            return None

        url = 'https://www.bungie.net' + json['Response']['mobileWorldContentPaths']['en']
        await self._download_coroutine(url)


    async def _download_coroutine(self, url):
        """Download file at the given URL"""
        with async_timeout.timeout(10):
            async with self.api.session.get(url) as response:
                filename = os.path.basename(url)
                with open(filename, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f_handle.write(chunk)
                return await response.release()
