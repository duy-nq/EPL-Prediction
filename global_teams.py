import aiohttp
import asyncio
from understat import Understat
from support import export_to_csv

FILENAME = 'teams_1516_2223'
seasons = [2015,2016,2017,2018,2019,2020,2021,2022]

async def get_teams(season: list[int]) -> list:
    results = []
    
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        for season in seasons:
            teams = await understat.get_teams(
                "epl",
                season
            )

            for team in teams:
                result = (team['id'], team['title'])

                if result not in results:
                    results.append(result)
                else:
                    pass

    return results

def main():
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_teams(seasons))

    cols_name = ['id', 'title']

    export_to_csv(FILENAME, cols_name, data)

if __name__ == "__main__":
    main()

