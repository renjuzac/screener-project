from stocks import fetch


def test_get_stocks_with_growth_over():

    stocks_with_10per_growth  = fetch.get_stocks_with_revenue_growth_over("0.1")

    assert type(stocks_with_10per_growth) == dict
    assert (len(stocks_with_10per_growth) > 0) == True
