from datetime import timedelta

import requests
import requests_cache

expire_after = timedelta(hours=24)
session = requests_cache.CachedSession(cache_name='.api_cache',backend='sqlite',expire_after=expire_after)

