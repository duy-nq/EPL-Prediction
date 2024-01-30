data = {
    "h": {
        "341628": {
            "id": "341628",
            "goals": "2",
            "own_goals": "0",
            "shots": "4",
            "xG": "1.3030972480773926",
            "time": "88",
            "player_id": "556",
            "team_id": "89",
            "position": "AML",
            "player": "Marcus Rashford",
            "h_a": "h",
            "yellow_card": "0",
            "red_card": "0",
            "roster_in": "341631",
            "roster_out": "0",
            "key_passes": "0",
            "assists": "0",
            "xA": "0",
            "xGChain": "1.1517746448516846",
            "xGBuildup": "0.6098462343215942",
            "positionOrder": "13"
        },
        "341629": {
            "id": "341629",
            "goals": "1",
            "own_goals": "0",
            "shots": "4",
            "xG": "0.7688590884208679",
            "time": "90",
            "player_id": "553",
            "team_id": "89",
            "position": "FW",
            "player": "Anthony Martial",
            "h_a": "h",
            "yellow_card": "1",
            "red_card": "0",
            "roster_in": "0",
            "roster_out": "0",
            "key_passes": "1",
            "assists": "0",
            "xA": "0.05561231076717377",
            "xGChain": "0.9395027160644531",
            "xGBuildup": "0.11503136157989502",
            "positionOrder": "15"
        }
    },
    "a": {
        "341633": {
            "id": "341633",
            "goals": "0",
            "own_goals": "0",
            "shots": "0",
            "xG": "0",
            "time": "90",
            "player_id": "5061",
            "team_id": "80",
            "position": "GK",
            "player": "Kepa",
            "h_a": "a",
            "yellow_card": "0",
            "red_card": "0",
            "roster_in": "0",
            "roster_out": "0",
            "key_passes": "0",
            "assists": "0",
            "xA": "0",
            "xGChain": "0.04707280918955803",
            "xGBuildup": "0.04707280918955803",
            "positionOrder": "1"
        },
        "341642": {
            "id": "341642",
            "goals": "0",
            "own_goals": "0",
            "shots": "2",
            "xG": "0.08609434962272644",
            "time": "60",
            "player_id": "592",
            "team_id": "80",
            "position": "AML",
            "player": "Ross Barkley",
            "h_a": "a",
            "yellow_card": "0",
            "red_card": "0",
            "roster_in": "341646",
            "roster_out": "0",
            "key_passes": "1",
            "assists": "0",
            "xA": "0.024473881348967552",
            "xGChain": "0.11056823283433914",
            "xGBuildup": "0",
            "positionOrder": "13"
        }
    }
}

# Extract player_ids
player_ids = []

for team in data.values():
    for player_data in team.values():
        player_ids.append(player_data["player_id"])

print(player_ids)