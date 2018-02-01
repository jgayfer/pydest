import pytest
import asyncio
import json

import pydest


with open('credentials.json') as f:
    api_key = json.load(f)['api-key']


class BaseTestClass(object):

    _membership_id = 4611686018467257491
    _membership_type = 4

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7
    
    @pytest.mark.asyncio
    async def test_error_code_true(self, res):
        assert res['ErrorCode'] == 1


class TestGetBungieNetUserById(BaseTestClass):

    @pytest.fixture
    @pytest.mark.asyncio
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_bungie_net_user_by_id(637429)
        destiny.close()
        return r


class TestGetMembershipDataById(BaseTestClass):

    @pytest.fixture
    @pytest.mark.asyncio
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_membership_data_by_id(637429)
        destiny.close()
        return r


class TestGetDestinyManifest(BaseTestClass):

    @pytest.fixture
    @pytest.mark.asyncio
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_destiny_manifest()
        destiny.close()
        return r


class TestSearchDestinyPlayer(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.search_destiny_player(1, 'dummy')
        destiny.close()
        return r


class TestGetProfile(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_profile(self._membership_type, self._membership_id, ['Characters'])
        destiny.close()
        return r


class TestGetCharacter(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        profile = await destiny.api.get_profile(self._membership_type, self._membership_id, ["Characters"])
        res = profile['Response']['characters']['data']
        character_hash = ""
        for item in res:
            character_hash = item
            break

        r = await destiny.api.get_character(self._membership_type, self._membership_id, character_hash, ['CharacterActivities'])
        destiny.close()
        return r


class TestGetClanWeeklyRewardState(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        res = await destiny.api.get_groups_for_member(self._membership_type, self._membership_id)
        group_id = res['Response']['results'][0]['member']['groupId']
        r = await destiny.api.get_clan_weekly_reward_state(group_id)
        destiny.close()
        return r


class TestGetItem(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_item(self._membership_type, self._membership_id, '1048266744', ['ItemCommonData'])
        destiny.close()
        return r


class TestGetPostGameCarnageReport(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_post_game_carnage_report('123')
        destiny.close()
        return r


class TestGetHistoricalStatsDefinition(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_historical_stats_definition()
        destiny.close()
        return r


class TestGetPublicMilestoneContent(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_public_milestone_content('123')
        destiny.close()
        return r


class TestGetPublicMilestones(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_public_milestones()
        destiny.close()
        return r


class TestGetGroupForMember(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_groups_for_member(1, 4611686018467257491)
        destiny.close()
        return r


class TestGetMilestoneDefinitions(BaseTestClass):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        milestone_r = await destiny.api.get_public_milestones()
        ms = milestone_r['Response']
        milestone_hash = ""
        for item in ms:
            milestone_hash = item
            break
            
        r = await destiny.api.get_milestone_definitions(milestone_hash)
        destiny.close()
        return r
        