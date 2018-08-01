from datetime import timedelta

import requests
import requests_cache

import redis


expire_after = timedelta(hours=1)
session = requests_cache.CachedSession(cache_name='.api_cache', backend='sqlite', expire_after=expire_after)


# r = redis.StrictRedis(host='cod.redistogo.com', port=11522,  password = "53ad9ac32374caa56f0483cdad9f8c7e")
# session = requests_cache.CachedSession( cache_name='cache' ,backend='redis' , connection = r)

# https://redis-py.readthedocs.io/en/latest/
# https://requests-cache.readthedocs.io/en/latest/api.html#requests_cache.core.CachedSession
# https://requests-cache.readthedocs.io/en/latest/api.html#backends-redis