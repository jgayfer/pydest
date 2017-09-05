import pydest
import asyncio


async def main():
    destiny = pydest.Pydest('api-key')
    activity = await destiny.decode_hash(-2028012773, 'DestinyActivityDefinition')
    print("Activity Name: {}".format(activity['displayProperties']['name']))
    print("Description: {}".format(activity['displayProperties']['description']))
    destiny.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
