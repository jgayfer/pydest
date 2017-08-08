from api import API
from models.account import Account

class Destiny:

    def __init__(self, api_key):
        self.api = API(api_key)


    async def get_account(self, membership_type, display_name):
        json = await self.api.search_destiny_player(membership_type, display_name)
        return Account(json)
