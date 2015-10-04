import os

DATABASE = {
    'drivername': os.environ['DB_DRIVER'],
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'username': os.environ['DB_USER'],
    'database': os.environ['DB_NAME'],
}
