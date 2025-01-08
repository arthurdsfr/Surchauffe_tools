import data.recover_data.coingecko_api

eth_prices, market_cap, volume_trading_24h = data.recover_data.coingecko_api.fetch_eth_datas(365)

print(len(eth_prices))
print(len(market_cap))
print(len(volume_trading_24h))

#def price_variation_1d(eth_prices_365j):
