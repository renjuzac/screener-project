from stocks import scan
from stocks import fetch

stocks = scan.scan_on_growth_volume_price()

high_growth = fetch.get_stocks_with_revenue_growth_over("0.3")
volume_price = fetch.get_stock_price_and_vol([])

for ticker in stocks:
    print ("{} {}  {}".format(ticker,volume_price[ticker],high_growth[ticker]))

