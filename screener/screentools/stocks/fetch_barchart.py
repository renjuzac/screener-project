# https://www.barchart.com/ondemand/api/getQuote/free

import json

from caching import session


#from ..config import barchart_api_key

barchart_api_key = "62ee527bc88e5383f47f67b551d75bda"

symbols = ['AAPL', 'GOOGL']
fields = ["fiftyTwoWkHigh","fiftyTwoWkLow","avgVolume","twentyDayAvgVol"]


def getquote(symbols=symbols,fields=fields):

    getquote_url = "https://marketdata.websol.barchart.com/getQuote.json?apikey={apikey}&symbols={symbolnames}&fields={fieldnames}"


    symbolnames = ""
    for ticker in symbols:
        symbolnames = symbolnames + "%2C" + ticker

    fieldnames = ""

    for field in fields:
        fieldnames = fieldnames + "%2C" + field

    getquote_url = getquote_url.format(apikey=barchart_api_key,symbolnames=symbolnames,fieldnames=fieldnames)
    data = session.get(getquote_url)
    jsondata = json.loads(data.text)

    return(jsondata['results'])

# Fields seperated by %2C

if __name__ == "__main__" :
    quotes = getquote()
    print(quotes)
