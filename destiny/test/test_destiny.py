import unittest
import asyncio
from unittest.mock import patch
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from destiny import Destiny
import destiny
from destiny.test.data import responses

patch('destiny.api', lambda x: x).start()

class TestGetAccount(unittest.TestCase):

    def setUp(self):
        self.d = Destiny('dumb')
        self.loop = asyncio.get_event_loop()

    def tearDown(self):
        self.loop.close()

    @patch('destiny.destiny.api.search_destiny_player', new=responses.x())
    def test_account_found(self):
        async def test():
            #mock_api_call.return_value = responses.search_destiny_player_ok
            account = await self.d.find_account(1, 'dummy')
            self.assertIsNotNone(account)
        self.loop.run_until_complete(test())





if __name__ == "__main__":
    unittest.main()
