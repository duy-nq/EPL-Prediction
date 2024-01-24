import asyncio
import json

import aiohttp

from understat import Understat

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        results = await understat.get_team_results(
            "Arsenal",
            2022,
            side="h"
        )
        print(json.dumps(results))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())