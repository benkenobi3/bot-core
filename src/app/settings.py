PORT: int = int(os.environ.get('PORT', '80'))
LOG_LEVEL: str = 'debug'


# Redis as broker
# Redis https://redis.io/
TASKS_REDIS = {
    'HOST': os.environ.get('TASKS_REDIS_HOST', 'tasks'),
    'PORT': os.environ.get('TASKS_REDIS_PORT', '6379')
}


# Redis as database
# Redis https://redis.io/
GAMES_REDIS = {
    'HOST': os.environ.get('GAMES_REDIS_HOST', 'games'),
    'PORT': os.environ.get('GAMES_REDIS_PORT', '6379')
}
