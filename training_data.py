import asyncio
import json

import aiohttp

from understat import Understat

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        starting_xi = await understat.get_match_players("18579")

        print(starting_xi)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())