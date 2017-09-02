import aiohttp
import async_timeout
import os
import zipfile

from pydest.api import API
from pydest.manifest import Manifest


class Pydest:

    def __init__(self, api_key):
        self.session = aiohttp.ClientSession()
        self.api = API(api_key, self.session)
        self.manifest = Manifest(self.api)


    async def decode_hash(self, hash_id, definition):
        """Get the corresponding static info for an item given it's hash value

        Args:
            hash_id:
                The unique identifier of the entity to decode
            definition:
                The type of entity to be decoded (ex. 'DestinyClassDefinition')

        Returns:
            dict: json corresponding to the given hash_id and definition

        Raises:
            PydestException
        """
        return await self.manifest.decode_hash(hash_id, definition)


    def close(self):
        self.session.close()


class PydestException(Exception):
    pass
