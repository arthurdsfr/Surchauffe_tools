import pandas as pd
import data.recover_data.coingecko_api as cg
import matplotlib.pyplot as plt
def rsi(coin_prices_365j):
    period = 14
    df_coin_prices_365j = pd.DataFrame(coin_prices_365j, columns=['Close'])
    price_delta_day = df_coin_prices_365j['Close'].diff()

    gain = price_delta_day.where(price_delta_day > 0, 0)
    losses = abs(price_delta_day.where(price_delta_day < 0, 0))

    ema_gain = gain.ewm(span=period, adjust=False).mean()
    ema_losses = losses.ewm(span=period, adjust=False).mean()

    relative_strength = ema_gain/ema_losses
    rsi = 100 - 100/(1+relative_strength)

    return rsi

#eth_prices, market_cap, volume_trading_24h = cg.fetch_eth_datas(365)
#rsi = rsi(eth_prices)
#plt.figure(figsize=(10, 5))
#plt.plot(rsi, label="rsi", color="blue")
#plt.title("Évolution du prix de l'Ethereum sur les 365 derniers jours")
#plt.xlabel("Jour")
#plt.ylabel("Prix en USD")
#plt.legend()
#plt.grid(True)
#plt.savefig('graph_eth_rsi')