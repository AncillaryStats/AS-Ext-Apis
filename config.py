import os
import redis

DATABASE = {
    'drivername': os.environ['DB_DRIVER'],
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'username': os.environ['DB_USER'],
    'database': os.environ['DB_NAME'],
    'password': os.environ['DB_PW']
}

redis_url = os.getenv('REDISTOGO_URL')
r = redis.StrictRedis.from_url(redis_url)
