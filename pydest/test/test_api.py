import pytest
import asyncio

import pydest


class TestGetDestinyManifest(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_destiny_manifest()

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestSearchDestinyPlayer(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.search_destiny_player(1, 'dummy')

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetProfile(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_profile(1, '123', ['Characters'])

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetCharacter(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_profile(1, '123', '123')

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetClanWeeklyRewardState(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_clan_weekly_reward_state('123')

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetItem(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_item(1, '123', '123', ['ItemCommonData'])

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetPostGameCarnageReport(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_post_game_carnage_report('123')

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetHistoricalStatsDefinition(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_historical_stats_definition()

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetPublicMilestoneContent(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_public_milestone_content('123')

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1


class TestGetPublicMilestones(object):

    @pytest.mark.asyncio
    @pytest.fixture
    async def res(self):
        with pydest.API('2ead071ad8c643559032dc155ee21170') as destiny:
            return await destiny.get_public_milestones()

    @pytest.mark.asyncio
    async def test_is_dict(self, res):
        assert type(res) is dict

    @pytest.mark.asyncio
    async def test_error_code(self, res):
        assert res['ErrorCode'] == 1
