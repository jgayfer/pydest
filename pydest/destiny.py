from pydest.api import API
from pydest.models.account import Account


class Destiny:

    def __init__(self, api_key):
        self.api = API(api_key)


    async def get_account(self, membership_type, display_name):
        """Return a Destiny 2 Account object. None if not found"""
        json = await self.api.search_destiny_player(membership_type, display_name)

        if json['ErrorCode'] != 1:
            return None

        membership_id = json['Response'][0]['MembershipId']
        json = await self.api.get_profile(membership_type, membership_id)

        if json['ErrorCode'] != 1:
            return None
        else:
            return Account(json)
