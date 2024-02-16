from support import *

COLS_NAME = ['h_str', 'a_str', 'hth', 'h_poise', 'a_poise', 'result']

matches = read_csv('final_results/02.csv')

data = []
matches_id = []
results = []
hth_poise = []

for match in matches:
    if int(match[4]) > int(match[5]):
        results.append('WIN')
    elif int(match[4]) == int(match[5]):
        results.append('DRAW')
    else:
        results.append('LOSE')

    matches_id.append(match[0])
    hth_poise.append([float(match[6]), float(match[7]), head_to_head(match[2], match[3], match[1][:10])])

for id in matches_id:
    data.append([val for val in calc_team_strength(str(id))])

for i in range(len(data)):
    data[i] += hth_poise[i]
    data[i].append(results[i])

export_to_csv('training_data.csv', COLS_NAME, data)