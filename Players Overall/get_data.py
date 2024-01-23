from urllib import request
import re
import csv

version = [
    '/fifa16_73',
    '/fifa17_173',
    '/fifa18_278',
    '/fifa19_353',
    '/fifa20_419',
    '/fifa21_486',
    '/fifa22_555',
    '/fifa23_589',
    ''
]
position = {
    'GK': 'GK',
    'SW': 'DEF',
    'RWB': 'DEF',
    'LWB': 'DEF',
    'RB': 'DEF',
    'LB': 'DEF',
    'CB': 'DEF',
    'CDM': 'MID',
    'CM': 'MID',
    'LM': 'MID',
    'RM': 'MID',
    'CAM': 'MID',
    'CF': 'ATK',
    'ST': 'ATK',
    'LW': 'ATK',
    'RW': 'ATK'
}

pre_link = 'https://www.fifaindex.com/players'
page = '/?page='
last = '&?gender=0&league=13&order=desc'

def decoded_string(bytes_name: bytes) -> str:
    encoded_data = bytes_name
    decoded_data = encoded_data.decode('utf-8')

    return decoded_data

def get_name(name: list[str]) -> list[str]:
    only_names = []
    
    for n in name:
        n = n.replace('class="link-player">','')
        n = n[:-4]
        n = bytes(n, 'utf-8')

        n = n.decode('unicode_escape').encode("raw_unicode_escape")

        only_names.append(decoded_string(n))

    return only_names

def get_overall(stats: list[str]) -> list[int]:
    ovr = [stats[i] for i in range(len(stats)) if i%2 == 0]

    ovr_int = [int(ovr_i[-9:-7]) for ovr_i in ovr]

    return ovr_int

def get_club(clubs: list[str]) -> list[str]:
    only_clubs = []
    
    for club in clubs:
        club_name = club[7:club.find(' FIFA')]
        
        if (len(club_name) > 25):
            club_name = club_name[club_name.find('title="')+7:]

        only_clubs.append(club_name)

    return only_clubs

def export_to_csv(file_name: str, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(['player_name', 'overall', 'club'])

        writer.writerows(data)

def get_data():
    player_names = []
    overall = []
    clubs = []

    for i in range(29):
        link = pre_link + version[7] + page + str(i+1) + last

        req = request.Request(
            url=link,
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        try:
            info = request.urlopen(req).read()
        except:
            break

        string_info = str(info)

        name = re.findall('class="link-player">.{,90}</a>', string_info)
        stats = re.findall('<span class="badge badge-dark rating ..">[0-9]{,3}</span>', string_info)
        club_page = re.findall('title=".{,60} FIFA .." class="link-team">', string_info)

        player_names += get_name(name)
        overall += get_overall(stats)
        clubs += get_club(clubs=club_page)

    return list(zip(player_names, overall, clubs))

def main():
    data = get_data()
    export_to_csv('players_2324', data)

if __name__ == '__main__':
    main()
