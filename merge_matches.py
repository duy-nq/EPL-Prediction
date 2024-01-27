import asyncio
import json
import aiohttp
from understat import Understat
import csv

new_labels = ['h_p_1','h_p_2','h_p_3','h_p_4','h_p_5','h_p_6','h_p_7','h_p_8','h_p_9','h_p_10','h_p_11',
              'a_p_1','a_p_2','a_p_3','a_p_4','a_p_5','a_p_6','a_p_7','a_p_8','a_p_9','a_p_10','a_p_11']

async def get_players_in_match(match_id: int):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_match_players(match_id)
        return players
def get_player_ids(players_data:list):
    player_ids = []
    for team in players_data.values():
        for player_data in team.values():
            if(player_data['position']=='Sub'):continue
            player_ids.append(player_data["player_id"])
    return player_ids


csv_file_path = 'Results/results_1516_2223.csv'
output_csv_file_path = 'final_results/01.csv'
with open(csv_file_path, 'r') as csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_csv_file)
    header = next(csv_reader, None)
    if header:
        csv_writer.writerow(header + new_labels)
    count = 0
    for row in csv_reader:
        loop = asyncio.get_event_loop()
        players = loop.run_until_complete(get_players_in_match(row[0]))
        player_ids = get_player_ids(players)
        row_with_player_ids = row + player_ids
        csv_writer.writerow(row_with_player_ids)
        count+=1
        print(count)
print(f'Data written to: {output_csv_file_path}')

       