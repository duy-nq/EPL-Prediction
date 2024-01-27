from support import read_csv, export_to_csv, match_strings

PLAYER_COLS = ['id', 'name', '1516', '1617', '1718', '1819', '1920', '2021', '2122', '2223']

SEASONS = [
    'players_1516',
    'players_1617',
    'players_1718',
    'players_1819',
    'players_1920',
    'players_2021',
    'players_2122',
    'players_2223',
]

def player_overall():
    col_num = 2
    filename_players = 'Players Overall/players_1516_2223.csv'

    players_data = read_csv(filename_players)
    players_only = [pd_i[1] for pd_i in players_data]
    unmatched_players = []
    
    for season in SEASONS:
        filename_ovr = 'Players Overall/' + season + '.csv'
        
        ovr_data = read_csv(filename_ovr)

        for ovr_i in ovr_data:
            try:
                players_data[players_only.index(ovr_i[0])][col_num] = ovr_i[1]
            except:
                tmp = ovr_i + [int(season[8:10])-13]
                unmatched_players.append(tmp)

        col_num += 1

    for up_i in unmatched_players:
        for pd_i in players_only:
            if match_strings(up_i[0], pd_i):
                players_data[players_only.index(pd_i)][up_i[3]] = up_i[1]

    return players_data, unmatched_players

def main():
    ovr, unmatch = player_overall()

    export_to_csv('players_overall_1516_2223', PLAYER_COLS, ovr)

if __name__ == '__main__':
    main()
