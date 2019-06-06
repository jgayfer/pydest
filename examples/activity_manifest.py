import pydest
import asyncio


async def main():
    """You will need to add your api key!"""
    destiny = pydest.Pydest('api-key')

    activity1 = await destiny.decode_hash(60002467, 'DestinyActivityDefinition')
    await destiny.update_manifest()
    activity2 = await destiny.decode_hash(80726883, 'DestinyActivityDefinition')

    print("Activity Name: {}".format(activity1['displayProperties']['name']))
    print("Description: {}".format(activity1['displayProperties']['description']))
    print("")
    print("Activity Name: {}".format(activity2['displayProperties']['name']))
    print("Description: {}".format(activity2['displayProperties']['description']))

    await destiny.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
