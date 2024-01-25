import csv

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

def calc_team_strength(match_id: str) -> tuple[float, float]:
    """
    Returns an estimate of the strength of the home and away teams
    """

    h_str = 0
    a_str = 0

    # Add your code here...

    return (h_str, a_str)

def last_5_matches(team_id: str) -> int:
    """
    Return team's form in last 5 matches
    """

    points = 0

    # Add your code here...

    return points

def last_5_matches_at(team_id: str, at_home: bool) -> int:
    """
    Return the team performance (home/away) in last 5 matches
    """

    points = 0

    # Add your code here

    return points

def head_to_head(home_id: str, away_id: str) -> int:
    """
    Return some head_to_head result(s) between two teams
    """

    # Add your code here

    return 0