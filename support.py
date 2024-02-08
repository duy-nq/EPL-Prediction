import csv
from fuzzywuzzy import fuzz

def match_strings(str1, str2, threshold=90):
    similarity_ratio = fuzz.ratio(str1.lower(), str2.lower())
    return similarity_ratio >= threshold

def export_to_csv(file_name: str, cols_name: list[str] , data):
        """
        Write data into file with cols_name and custom data
        """
        
        assert len(data) != 0, "Your data is empty!"
        assert len(cols_name) == len(data[0]), "Num of cols_name need to be the same with num of cols in data"

        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(cols_name)

            writer.writerows(data)

def read_csv(filename: str) -> list:
    """
    Return data from .csv file
    """

    assert filename != "", "File name is empty!"
    
    file = open(filename, 'r', encoding='utf-8')

    csv_reader = csv.reader(file)
    
    next(csv_reader)

    data = [row for row in csv_reader]

    return data 

def calc_team_strength(match_id: str) -> tuple[float, float]:
    """
    Returns an estimate of the strength of the home and away teams
    """

    players = read_csv('Players Overall/players_overall_1516_2223.csv')
    only_players_id = [player[0] for player in players]

    matches = read_csv('final_results/01.csv')
    only_matches_id = [match[0] for match in matches]

    #[6:17] [17:] via data in final results
    h_ovr = []
    a_ovr = []

    match_index = only_matches_id.index(match_id)
    h_players = matches[match_index][6:17]
    a_players = matches[match_index][17:]

    date = str(matches[match_index][1])[:11]

    year = date[:4]
    season_col = 0

    if int(date[5:7]) <= 6:
        season_col = int(year)-2014
    else:
        season_col = int(year)-2013

    for player in h_players:
        player_index = only_players_id.index(player)
        h_ovr.append(int(players[player_index][season_col]))

    for player in a_players:
        player_index = only_players_id.index(player)
        a_ovr.append(int(players[player_index][season_col]))

    print(h_ovr, a_ovr)

    return (sum(h_ovr), sum(a_ovr))

def last_5_matches_at(team_id: str, at_home: bool, date:str) -> int:
    """
    Return the team performance (home/away) in last 5 matches
    """
    temp_list = []
    data = read_csv('Results/results_1516_2223.csv')
    for row in data:
        if row[1]>=date: break
        if at_home:
            if(row[2]!=team_id): continue
            if(row[4]>row[5]):
                #win
                temp_list.append(3)
            elif(row[4]<row[5]):
                #loss
                temp_list.append(0)
                pass
            elif(row[4]==row[5]):
                #draw
                temp_list.append(1)
        else:
            if(row[3]!=team_id): continue
            if(row[4]<row[5]):
                # win
                temp_list.append(3)
            elif(row[4]>row[5]):
                # loss
                temp_list.append(0)
            elif(row[4]==row[5]):
                #draw
                temp_list.append(1)
        
        if len(temp_list)==6:
            temp_list.pop(0)
    if len(temp_list)==0: return 0
    return sum(temp_list)/len(temp_list)

def head_to_head(home_id: str, away_id: str, date: str) -> float:
    """
    Return some head_to_head result(s) (average points) between two teams

    date: '2021-12-24'
    """

    pattern = [[home_id, away_id], [away_id, home_id]]

    points = 0
    versus = 0

    matches = read_csv('Results/results_1516_2223.csv')
    
    for match in matches[::-1]:
        if match[2:4] in pattern and match[1][:10] < date:
            versus += 1
            
            if match[4] == match[5]:
                points += 1
                continue
            if match[2:4] == pattern[0] and match[4] > match[5]:
                points += 3
            elif match[2:4] == pattern[1] and match[4] < match[5]:
                points += 3

        if (versus == 5):
            break    

    return points/versus