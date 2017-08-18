import asyncio
import pytest
from unittest.mock import MagicMock

import destiny
from destiny.test.data import responses


class TestGetAccount(object):

    @pytest.mark.asyncio
    async def test_account_found(self):

        mock = MagicMock()
        mock.method.return_value = responses.account_found
        execute_coro = asyncio.coroutine(mock.method)

        wrapper = destiny.Destiny('dummy')
        wrapper.api.search_destiny_player = execute_coro
        account = await wrapper.get_account(-1, 'dummy_user')

        assert account != None


    @pytest.mark.asyncio
    async def test_account_not_found(self):

        mock = MagicMock()
        mock.method.return_value = responses.account_not_found
        execute_coro = asyncio.coroutine(mock.method)

        wrapper = destiny.Destiny('dummy')
        wrapper.api.search_destiny_player = execute_coro
        account = await wrapper.get_account(-1, 'dummy_user')

        assert account == None
