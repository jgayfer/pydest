import aiohttp
import asyncio

from pydest.api import API
from pydest.manifest import Manifest


class Pydest:

    def __init__(self, api_key):
        self.api_key = api_key


    async def manifest_db(self):
        with API(self.api_key) as api:
            json = await api.get_destiny_manifest()
            if json['ErrorCode'] == 1:
                return Manifest(json)
