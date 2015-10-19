import redis
import os
import time
import run
import json
from queue import RedisQueue
from config import r

trend_q = RedisQueue('trending', r)
trend_store = 'trending_store'

while True:
    print 'checking work queue'
    message = trend_q.dequeue()
    print message
    # get trending players
    if message[1] == 'GET TRENDING PLAYERS':
        results = run.trending_players()
        print results
        r.set(trend_store, json.dumps(results))
    time.sleep(2)
