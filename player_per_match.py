import asyncio
import json
import aiohttp
from understat import Understat

async def main(player_id:int):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_match_players(player_id)
        return players

for i in range(81, 85):
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(main(i))
    # Get the list of player IDs for both home and away teams
    home_team_player_ids = [player_info["player_id"] for player_info in data["h"].values() if player_info['position'] != 'Sub']
    away_team_player_ids = [player_info["player_id"] for player_info in data["a"].values() if player_info['position'] != 'Sub']

    print(home_team_player_ids)
    print(away_team_player_ids)
    # # Combine player IDs from both teams
    # all_player_ids = home_team_player_ids + away_team_player_ids

    # # Count the distinct player IDs to get the total number of players
    # total_players = len(set(all_player_ids))

    # print("Total players in the match:", total_players)
