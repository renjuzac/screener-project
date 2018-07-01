# https://www.barchart.com/ondemand/api/getQuote/free

import requests
import json

from caching import session

#from config import barchart_api_key

barchart_api_key = "62ee527bc88e5383f47f67b551d75bda"

getquote_url = "https://marketdata.websol.barchart.com/getQuote.json?apikey={apikey}&symbols={symbolnames}&fields={fieldnames}"


symbols = ['AAPL','GOOGL']

symbolnames = ""
for ticker in symbols:
    symbolnames = symbolnames + "%2C" + ticker

fieldnames = ""
fields = ["fiftyTwoWkHigh","fiftyTwoWkLow","avgVolume","twentyDayAvgVol",]
for field in fields:
    fieldnames = fieldnames + "%2C" + field

getquote_url = getquote_url.format(apikey=barchart_api_key,symbolnames=symbolnames,fieldnames=fieldnames)
#data = requests.get(getquote_url)
data = session.get(getquote_url)
jsondata = json.loads(data.text)

print(jsondata['results'])

# Fields seperated by %2C
