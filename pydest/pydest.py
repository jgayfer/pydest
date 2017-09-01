import aiohttp
import asyncio
import async_timeout
import os
import zipfile

from pydest.api import API
from pydest.manifest import Manifest


class Pydest:

    def __init__(self, api_key):
        self.api = API(api_key)
        self.manifest_file = None


    async def decode_item(self, item_id, table):
        """Decode an item from the manifest"""
        if not self.manifest_file:
            self.manifest_file = await self._get_manifest_file()

        with Manifest(self.manifest_file) as manifest:
            json = manifest.query(table, item_id)
            if json:
                return json


    async def _get_manifest_file(self):
        """Create a new Manifest database object"""
        json = await self.api.get_destiny_manifest()

        if json['ErrorCode'] != 1:
            return None

        url = 'https://www.bungie.net' + json['Response']['mobileWorldContentPaths']['en']
        filename = await self._download_file(url)

        if os.path.isfile('./{}'.format('manifest_zip')):

            # Extract database file
            zip_ref = zipfile.ZipFile('./{}'.format('manifest_zip'), 'r')
            zip_ref.extractall('./')
            zip_ref.close()

            # Get name of database file
            with zipfile.ZipFile('manifest_zip', 'r') as f:
                return f.namelist()[0]


    async def _download_file(self, url):
        """Download file at the given URL"""
        with async_timeout.timeout(10):
            async with self.api.session.get(url) as response:
                filename = os.path.basename('manifest_zip')
                with open(filename, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f_handle.write(chunk)
                return await response.release()


    def close(self):
        self.api.close_session()
