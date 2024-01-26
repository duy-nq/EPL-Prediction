import asyncio

import aiohttp

from understat import Understat

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        players = await understat.get_league_players(
            "epl",
            2023
        )

        print(players)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())