from stocks import scan
from stocks import fetch_intrinio

stocks = scan.scan_on_growth()

high_growth = fetch_intrinio.get_stocks_with_revenue_growth_over("0.3")
volume_price = fetch_intrinio.get_stock_price_and_vol([])

mytickers = {}

for ticker in stocks:
#    print ("{} {}  {}".format(ticker,volume_price[ticker],high_growth[ticker]))
    mytickers[ticker] = high_growth[ticker]

sortedtickers = sorted(mytickers, key=mytickers.__getitem__)

for ticker in sortedtickers:
    print("{}: {}   {}".format(ticker,volume_price[ticker] ,high_growth[ticker]))

print(sortedtickers)