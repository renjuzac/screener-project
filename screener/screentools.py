from screentools.stocks import scan
from screentools.stocks import fetch
from screentools.stocks import screendata




# stocks = scan.scan_on_growth()

#high_growth = fetch.get_stocks_with_revenue_growth_over("0.3")
#print(high_growth)
# volume_price = fetch.get_stock_price_and_vol([])

# mytickers = {}

# for ticker in stocks:
# #    print ("{} {}  {}".format(ticker,volume_price[ticker],high_growth[ticker]))
#     mytickers[ticker] = high_growth[ticker]

# sortedtickers = sorted(mytickers, key=mytickers.__getitem__)

# for ticker in sortedtickers:
#     print("{}: {}   {}".format(ticker,volume_price[ticker] ,high_growth[ticker]))

# print(sortedtickers)




# from screentools.stocks import fetch

growth_stocks_list =['LNKD', 'AM', 'MDVN', 'APC', 'HFC', 'DOC', 'WDAY', 'TXT', 'NFLX', 'DRE', 'SHW', 'DYAX', 'MPLX', 'WYNN', 'ZU', 'AMZN', 'SPLK', 'EOG', 'FMC', 'HAL', 'NOW', 'ZLTQ', 'AMTD', 'XEC', 'NTNX', 'O', 'CMC', 'PSTG', 'JUNO', 'GRUB', 'LRCX', 'HDP', 'BHI', 'W', 'TROX', 'NVDA', 'TMST', 'TSLA', 'WLTW', 'FB', 'HP', 'EXPD', 'CXO', 'ADI', 'TTD', 'WPX', 'PTXP', 'KIM', 'PXD', 'UCTT', 'ALNY', 'CRZO', 'PDCE', 'REG', 'AIV', 'MU', 'CLR', 'PYPL', 'SQ', 'EGN', 'RRC', 'MTDR', 'NXST', 'INCY', 'SCTY', 'TAP', 'AON', 'HTS', 'PE', 'RSPP', 'EQT', 'SLCA', 'CORT', 'NRZ', 'SBRA', 'FANG', 'EXEL', 'RICE', 'BCEI', 'EXAS', 'HALO', 'SGMO', 'NKTR', 'ANAC', 'LNG', 'PTEN', 'CNX', 'CNL', 'CBOE', 'TSRO', 'ACAD', 'FOLD', 'SRPT', 'CLVS']

stock_quotes  = fetch.getquote(symbols=growth_stocks_list)
# print(len(stock_quotes))
print(stock_quotes)

#stock_list =['JWN', 'NSC', 'OFG', 'OMAD', 'OMADU', 'PDI', 'PRTY', 'PFGC', 'PLNT', 'PRI', 'RLI', 'RWT', 'RWGEU', 'RMD', 'RST', 'RMT', 'SHAK', 'SHOP', 'SON', 'SQ']

#stock_list = ['KMDA', 'KNSL', 'LFACW', 'LANC', 'LACQU', 'LSXMA', 'LINDW', 'LIND', 'LOB', 'LOGI', 'MASI', 'MEDP', 'MSFT', 'MRTX', 'MOR', 'NOVT', 'NVCR', 'OFLX', 'FLWS', 'OSPR']

#stocklist = ['F']

# print("paypal",fetch.get_aq_multiple_stock('PYPL'))
# print("google",fetch.get_aq_multiple_stock('GOOGL'))
# print("sarepta",fetch.get_aq_multiple_stock('SRPT'))
# # print(fetch.get_metadata(stock_list))


# stk = fetch.get_stocks_with_declining_revenue(percent=0)
# print(list(stk.keys()))

# print(fetch.get_aq_multiple_stock_list(stock_list))

#print(fetch.get_revenue_growth(stocklist))

#print(fetch.get_enterprise_multiple(stock_list))
#print(fetch.get_debt_to_equity(stocklist))

#res = screendata.scan_for_momentum()

#print(res)


