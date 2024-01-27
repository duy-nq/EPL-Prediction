import aiohttp
import asyncio
from understat import Understat
from support import export_to_csv

FILENAME_RESULTS = 'results_1516_2223'
FILENAME_TEAMS = 'teams_1516_2223'
FILENAME_PLAYERS = 'players_1516_2223'

SEASONS = [2015,2016,2017,2018,2019,2020,2021,2022]

PLAYER_COLS = ['id', 'name', '1516', '1617', '1718', '1819', '1920', '2021', '2122', '2223']
TEAM_COLS = ['id', 'title']
RESULT_COLS = ['id', 'h_id', 'a_id', 'h_goals', 'a_goals']

async def get_teams() -> list:
    results = []
    
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        for season in SEASONS:
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

async def get_results() -> list:
    results = []
    
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        for season in SEASONS:
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

async def get_players() -> list:
    results = []
    
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        for season in SEASONS:
            players = await understat.get_league_players(
                "epl",
                season
            )

            for player in players:
                result = (player['id'], player['player_name'], 0, 0, 0, 0, 0, 0, 0, 0)

                if result not in results:
                    results.append(result)
                else:
                    pass

    return results

def main():
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_players())

    export_to_csv(FILENAME_PLAYERS, PLAYER_COLS, data)