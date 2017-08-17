import aiohttp
import re

from destiny.utils import check_alphanumeric


BASE_URL = 'https://www.bungie.net/Platform/Destiny/'


async def _get_request(api_key, url):
    """Make an async GET request"""
    headers = {'X-API-KEY':'{}'.format(api_key)}
    async with aiohttp.get(url, headers=headers) as r:
        return await r.json()


async def search_destiny_player(api_key, membership_type, display_name):
    check_alphanumeric(membership_type, display_name)
    url = BASE_URL + 'SearchDestinyPlayer/{}/{}/'
    url = url.format(membership_type, display_name)
    return await _get_request(api_key, url)


async def get_account_summary(api_key, membership_type, membership_id):
    check_alphanumeric(membership_type, membership_id)
    url = BASE_URL + '{}/Account/{}/Summary/'
    url = url.format(membership_type, membership_id)
    return await _get_request(api_key, url)
