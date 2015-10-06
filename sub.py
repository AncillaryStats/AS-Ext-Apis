import redis
import os
import time
import run
from queue import RedisQueue

redis_url = os.getenv('REDISTOGO_URL')
trend_q = RedisQueue('trending', redis_url)

while True:
    print 'checking work queue'
    message = trend_q.dequeue()
    print message
    # get trending players
    if message[1] == 'GET TRENDING PLAYERS':
        run.get_trends()
    time.sleep(2)
