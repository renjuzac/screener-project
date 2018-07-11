#https://www.alphavantage.co/documentation/
from ..config import quandl_api_key

from datetime import timedelta


import json

from . import caching



def get_url(url):
    try:
        response = caching.session.get(url)
        results = json.loads(response.text)
        return results

    except Exception as e:
        print("Error fetching data from server :- {}".format( url))
        print ("Response string:{}".format(response.text))
        return {}

