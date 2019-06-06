import pytest
import asyncio
from unittest.mock import MagicMock

import pydest


class TestDecodeHash(object):

    @pytest.mark.asyncio
    async def test_decode_hash_called(self):
        mock = MagicMock()
        mock.method.return_value = None
        decode_hash_mock = asyncio.coroutine(mock.method)

        destiny = pydest.Pydest('123')
        destiny._manifest.decode_hash = decode_hash_mock
        res = await destiny.decode_hash(123, 'ActivityDefinition', language='fr')
        await destiny.close()

        mock.method.assert_called_with(123, 'ActivityDefinition', 'fr')


class TestUpdateManifest(object):

    @pytest.mark.asyncio
    async def test_update_manifest_called(self):
        mock = MagicMock()
        mock.method.return_value = None
        update_manifest_mock = asyncio.coroutine(mock.method)

        destiny = pydest.Pydest('123')
        destiny._manifest.update_manifest = update_manifest_mock
        res = await destiny.update_manifest(language='en')
        await destiny.close()

        mock.method.assert_called_with('en')


class TestClose(object):

    @pytest.mark.asyncio
    async def test_close(self):
        destiny = pydest.Pydest('123')
        await destiny.close()
        assert destiny._session.closed
