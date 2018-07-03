from stocks import  fetch_intrinio


def scan_on_growth():
    '''Scan for stocks based on growth percent , volume and price'''

    high_growth = fetch_intrinio.get_stocks_with_revenue_growth_over("0.3")
    volume_price = fetch_intrinio.get_stock_price_and_vol([])

    uniques = set(high_growth.keys()) & set(volume_price.keys())

    return list(uniques)

