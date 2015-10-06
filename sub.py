import redis
import os
import time
import run
from queue import RedisQueue
from config import r
trend_q = RedisQueue('trending', r)

while True:
    print 'checking work queue'
    message = trend_q.dequeue()
    print message
    # get trending players
    if message[1] == 'GET TRENDING PLAYERS':
        results = run.trending_players()
        print results
    time.sleep(2)
