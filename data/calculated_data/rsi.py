import pandas as pd


def rsi(coin_prices):
    period = 14
    df_coin_prices= pd.DataFrame(coin_prices, columns=['Close'])
    price_delta_day = df_coin_prices['Close'].diff()

    gain = price_delta_day.where(price_delta_day > 0, 0)
    losses = abs(price_delta_day.where(price_delta_day < 0, 0))

    ema_gain = gain.ewm(span=period, adjust=False).mean()
    ema_losses = losses.ewm(span=period, adjust=False).mean()

    relative_strength = ema_gain/ema_losses
    rsi = 100 - 100/(1+relative_strength)

    return rsi