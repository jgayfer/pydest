import aiohttp
import async_timeout
import os
import zipfile
import json
import sqlite3

import pydest
from pydest.dbase import DBase


MANIFEST_ZIP = 'manifest_zip'

class Manifest:

    def __init__(self, api):
        self.api = api
        self.manifest_files = {'en': '', 'fr': '', 'es': '', 'de': '', 'it': '', 'ja': '', 'pt-br': '', 'es-mx': '',
                               'ru': '', 'pl': '', 'zh-cht': ''}

    async def decode_hash(self, hash_id, definition, language):
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
        if language not in self.manifest_files.keys():
            raise pydest.PydestException("Unsupported language: {}".format(language))

        if self.manifest_files.get(language) == '':
            await self.update_manifest(language)

        # Identifier is different for the DestinyHistorialStatsDefinition table
        if definition == 'DestinyHistoricalStatsDefinition':
            hash_id = '"{}"'.format(hash_id)
            identifier = 'key'
        else:
            hash_id = self._twos_comp_32(hash_id)
            identifier = "id"

        with DBase(self.manifest_files.get(language)) as db:
            try:
                res = db.query(hash_id, definition, identifier)
            except sqlite3.OperationalError as e:
                if e.args[0].startswith('no such table'):
                    raise pydest.PydestException("Invalid definition: {}".format(definition))
                else:
                    raise e

            if len(res) > 0:
                return json.loads(res[0][0])
            else:
                raise pydest.PydestException("No entry found with id: {}".format(hash_id))


    async def update_manifest(self, language):
        """Download the latest manifest file for the given language if necessary

        Args:
            language:
                The language corresponding to the manifest to update

        Raises:
            PydestException
        """
        if language not in self.manifest_files.keys():
            raise pydest.PydestException("Unsupported language: {}".format(language))

        json = await self.api.get_destiny_manifest()
        if json['ErrorCode'] != 1:
            raise pydest.PydestException("Could not retrieve Manifest from Bungie.net")

        manifest_url = 'https://www.bungie.net' + json['Response']['mobileWorldContentPaths'][language]
        manifest_file_name = manifest_url.split('/')[-1]

        if not os.path.isfile(manifest_file_name):
            # Manifest doesn't exist, or isn't up to date
            # Download and extract the current manifest
            # Remove the zip file once finished
            filename = await self._download_file(manifest_url, MANIFEST_ZIP)
            if os.path.isfile('./{}'.format(MANIFEST_ZIP)):
                zip_ref = zipfile.ZipFile('./{}'.format(MANIFEST_ZIP), 'r')
                zip_ref.extractall('./')
                zip_ref.close()
                os.remove(MANIFEST_ZIP)
            else:
                raise pydest.PydestException("Could not retrieve Manifest from Bungie.net")

        self.manifest_files[language] = manifest_file_name


    async def _download_file(self, url, name):
        """Async file download

        Args:
            url (str):
                The URL from which to download the file
            name (str):
                The name to give to the downloaded file
        """
        with async_timeout.timeout(10):
            async with self.api.session.get(url) as response:
                filename = os.path.basename(name)
                with open(filename, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f_handle.write(chunk)
                return await response.release()


    def _twos_comp_32(self, val):
        val = int(val)
        if (val & (1 << (32 - 1))) != 0:
            val = val - (1 << 32)
        return val
