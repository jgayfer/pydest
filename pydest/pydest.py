import aiohttp
import async_timeout
import os
import zipfile
import asyncio

from pydest.api import API
from pydest.manifest import Manifest


class Pydest:

    def __init__(self, api_key, loop=None):
        """Base class for Pydest"""
        self._loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=self._loop)
        self.api = API(api_key, self._session)
        self._manifest = Manifest(self.api)


    async def decode_hash(self, hash_id, definition, language="en"):
        """Get the corresponding static info for an item given it's hash value from the Manifest

        Args:
            hash_id:
                The unique identifier of the entity to decode
            definition:
                The type of entity to be decoded (ex. 'DestinyClassDefinition')
            lanauge:
                The language to use when retrieving results from the Manifest

        Returns:
            dict: json corresponding to the given hash_id and definition

        Raises:
            PydestException
        """
        return await self._manifest.decode_hash(hash_id, definition, language)


    async def update_manifest(self, language='en'):
        """Update the manifest if there is a newer version available

        Args:
            language [optional]:
                The language corresponding to the manifest to update
        """
        await self._manifest.update_manifest(language)


    async def close(self):
        await self._session.close()


class PydestException(Exception):
    pass
