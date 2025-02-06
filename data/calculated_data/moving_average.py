import pandas as pd

def ema_50(coin_prices):
    serie_price = pd.Series(coin_prices)
    list_ema_50 = serie_price.ewm(span=50, adjust=False).mean()
    return list_ema_50

def sma_50(coin_prices):
    serie_price = pd.Series(coin_prices)
    list_ma_50 = serie_price.rolling(window=50, min_periods=1).mean()
    return list_ma_50

def ema_200(coin_prices):
    serie_price = pd.Series(coin_prices)
    list_ema_200 = serie_price.ewm(span=200, adjust=False).mean()
    return list_ema_200

def sma_200(coin_prices):
    serie_price = pd.Series(coin_prices)
    list_ma_200 = serie_price.rolling(window=200, min_periods=1).mean()
    return list_ma_200


