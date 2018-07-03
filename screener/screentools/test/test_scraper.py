import stocks.scraper as scraper

def test_stocks_52wk_high():
    tickers = scraper.stocks_52wk_highlow()
    assert (len(tickers['high'])>0)
    assert (len(tickers['low']) > 0)
    print(tickers['high'])
    print(tickers['low'])




