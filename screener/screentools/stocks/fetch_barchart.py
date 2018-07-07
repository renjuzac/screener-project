# https://www.barchart.com/ondemand/api/getQuote/free

import json

from screentools.stocks.caching import session
from screentools.config import barchart_api_key

barchart_api_key = "62ee527bc88e5383f47f67b551d75bda"

symbols = ['AAPL', 'GOOGL']
fields = ["fiftyTwoWkHigh", "fiftyTwoWkLow", "avgVolume", "twentyDayAvgVol"]


def getquote(symbols=symbols,fields=fields):
    '''
    Return a list containing a dictionary per ticker
    '''

    quotes = []

    fieldnames = ""

    for field in fields:
        fieldnames = fieldnames + "%2C" + field

    chunksize = 20      # Does not appear to have pagination support. 
    for i in range(0, len(symbols), chunksize):
        symbolchunk = symbols[i:i+chunksize]

        getquote_url = "https://marketdata.websol.barchart.com/getQuote.json?apikey={apikey}&symbols={symbolnames}&fields={fieldnames}"

        symbolnames = ""
        for ticker in symbolchunk:
            symbolnames = symbolnames + "%2C" + ticker

        getquote_url = getquote_url.format(apikey=barchart_api_key, symbolnames=symbolnames, fieldnames=fieldnames)
        data = session.get(getquote_url)
        jsondata = json.loads(data.text)

        quotes.extend(jsondata['results'])

    return(quotes)

# Fields seperated by %2C


