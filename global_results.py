import aiohttp
import csv
import asyncio
from understat import Understat

FILENAME = 'results_1516_2223'
seasons = [2015,2016,2017,2018,2019,2020,2021,2022]

async def get_results(season: list[int]) -> list:
    results = []
    
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        for season in seasons:
            fixtures = await understat.get_league_results(
                "epl",
                season
            )
                    
            for fixture in fixtures:
                result = (fixture['id'],
                          fixture['datetime'],
                          fixture['h']['id'],
                          fixture['a']['id'],
                          fixture['goals']['h'],
                          fixture['goals']['a']
                        )
                                
                results.append(result)

    print(results)
    return results

def export_to_csv(file_name: str, data):
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(['id', 'h_id', 'a_id', 'h_goals', 'a_goals'])

        writer.writerows(data)

def main():
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_results(seasons))

    export_to_csv(FILENAME, data)

if __name__ == "__main__":
    main()

