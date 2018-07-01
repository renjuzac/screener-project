import string

import stocks.scan as scan

def test_scan_on_growth_volume_price():
    result = scan.scan_on_growth_volume_price()
    assert type(result) == list
    assert (len(result) > 0) == True
    assert all([letter.lower() in set(string.ascii_lowercase) for letter in result[0]]) == True

    pass