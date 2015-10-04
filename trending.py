import requests
import config
import models
from sqlalchemy.orm import sessionmaker

params = { 'limit': '100' }
headers = { 'user-agent': 'ansel01@gmail.com '}


def top_titles():
    """Retrieves top 100 titles from /r/nfl and /r/fantasyfootball"""
    req_nfl = requests.get('http://www.reddit.com/r/nfl/.json', headers=headers, params=params)
    titles = []

    for item in req_nfl.json()['data']['children']:
        title = item['data']['title']
        title = title.encode('ascii','ignore')
        titles.append(str(title))

    req_ff = requests.get('http://www.reddit.com/r/fantasyfootball/.json', headers=headers, params=params)

    for item in req_ff.json()['data']['children']:
        title = item['data']['title']
        title = title.encode('ascii','ignore')
        titles.append(str(title))

    return ''.join(titles)

def get_players():
    """Gets player listings from db"""
    engine = models.db_connect()
    # models.create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    players = {}

    for player in session.query(models.NFL_Player_2015):
        players[str(player.name)] = 0

    session.close()

    return players

# print(trending_players())

def get_trends():
    """Returns sorted list of players with name occurances (if > 0)"""
    titles = top_titles()
    trending = []

    players = get_players()
    for name in players:
        count = titles.count(name)
        if count > 0:
            trending_player = { 'name': name, 'count': count}
            trending.append(trending_player)

    sorted_trending = sorted(trending, key=lambda x: x['count'], reverse=True)

    return sorted_trending


get_trends()