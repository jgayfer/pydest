import pytest
import asyncio
import json

import pydest


with open('credentials.json') as f:
    api_key = json.load(f)['api-key']


class TestGetBungieNetUserById(object):

    @pytest.fixture
    @pytest.mark.asyncio
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_bungie_net_user_by_id(637429)
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetDestinyManifest(object):

    @pytest.fixture
    @pytest.mark.asyncio
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_destiny_manifest()
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestSearchDestinyPlayer(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.search_destiny_player(1, 'dummy')
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict
        pass

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetProfile(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_profile(1, '123', ['Characters'])
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetCharacter(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_character(1, '123', '123', ['CharacterActivities'])
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetClanWeeklyRewardState(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_clan_weekly_reward_state('123')
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetItem(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_item(1, '123', '123', ['ItemCommonData'])
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetPostGameCarnageReport(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_post_game_carnage_report('123')
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetHistoricalStatsDefinition(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_historical_stats_definition()
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetPublicMilestoneContent(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_public_milestone_content('123')
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7


class TestGetPublicMilestones(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        destiny = pydest.Pydest(api_key)
        r = await destiny.api.get_public_milestones()
        destiny.close()
        return r

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] != 7
