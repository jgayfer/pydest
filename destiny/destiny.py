from destiny import api
from destiny.models.account import Account

class Destiny:

    def __init__(self, api_key):
        self.api_key = api_key


    async def find_account(self, membership_type, display_name):
        json = await api.search_destiny_player(self.api_key, membership_type, display_name)
        if json['ErrorCode'] == 1 and json['Response']:
            return Account(json)
