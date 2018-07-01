import re

import requests
from bs4 import BeautifulSoup


def stocks_52wk_highlow(high=True):
    '''
    List of stocks making new 52 week highs and lows

    return dict with list of high and low stocks
    {
     high:[],
     low:[]
    }
    '''

    HighStocks = []
    LowStocks = []

    nyse_url =  "http://www.wsj.com/mdc/public/page/2_3021-newhinyse-newhighs.html"
    nasdaq_url = "http://www.wsj.com/mdc/public/page/2_3021-newhinnm-newhighs.html"

    urls = [nyse_url,nasdaq_url]

    for dataurl in urls:

        page = requests.get(dataurl)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find("table",{"class":"mdcTable"})


        Highs = True

        for row in table.find_all('td'):
            atag = row.find('a', href=True)
            if  "Lows" in row.text:
                Highs = False
            if atag and Highs:
                HighStocks.append(atag['href'].split("=")[1])
            elif atag and not Highs:
                LowStocks.append(atag['href'].split("=")[1])

    results = {}

    results['high'] = HighStocks
    results['low'] = LowStocks

    return results


if __name__ == "__main__":
    tickers = stocks_52wk_highlow()
    print(tickers['high'])
    print(tickers['low'])


#    Return whole table without split
#    for atag in table.find_all('a', href=True):
#    print(atag['href'].split("=")[1])

#    stocks = [atag['href'].split("=")[1] for atag in table.find_all('a', href=True)]
#    URL: /public/quotes/main.html?symbol=CVIA
