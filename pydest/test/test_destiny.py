import asyncio
import pytest
from unittest.mock import MagicMock

import pydest
from pydest.test.data import responses


class TestGetAccount(object):

    @pytest.mark.asyncio
    async def test_account_found(self):

        mock = MagicMock()
        mock.method.return_value = responses.account_found
        execute_coro = asyncio.coroutine(mock.method)

        destiny = pydest.Destiny('dummy')
        destiny.api.search_destiny_player = execute_coro
        account = await destiny.get_account(-1, 'dummy_user')

        assert account != None


    @pytest.mark.asyncio
    async def test_account_not_found(self):

        mock = MagicMock()
        mock.method.return_value = responses.account_not_found
        execute_coro = asyncio.coroutine(mock.method)

        destiny = pydest.Destiny('dummy')
        destiny.api.search_destiny_player = execute_coro
        account = await destiny.get_account(-1, 'dummy_user')

        assert account == None
