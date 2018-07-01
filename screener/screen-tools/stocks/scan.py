from stocks import  fetch


def scan_on_growth_volume_price():
    '''Scan for stocks based on growth percent , volume and price'''

    high_growth = fetch.get_stocks_with_revenue_growth_over("0.3")
    volume_price = fetch.get_stock_price_and_vol([])

    uniques = set(high_growth.keys()) & set(volume_price.keys())

    return list(uniques)

