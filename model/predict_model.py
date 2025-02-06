import data.calculated_data.rsi as rs
import data.calculated_data.moving_average as ma
import data.calculated_data.variation_price as vp
import pandas as pd
from joblib import load
from data.recover_data.coin_from_excel import *


# Fonction pour faire des prédictions
def predict_model(coin_prices, number_trades, volume_24h):
    # Calculer les mêmes caractéristiques que pendant l'entraînement
    rsi = rs.rsi(coin_prices)
    sma50 = ma.sma_50(coin_prices)
    sma200 = ma.sma_200(coin_prices)
    ema50 = ma.ema_50(coin_prices)
    ema200 = ma.ema_200(coin_prices)
    vp_1d = vp.price_variation_1d(coin_prices)
    vp_7d = vp.price_variation_7d(coin_prices)
    vp_30d = vp.price_variation_30d(coin_prices)

    # Créer le DataFrame avec les caractéristiques calculées
    df = pd.DataFrame({
        'Close': coin_prices,
        'Number of Trades': number_trades,
        'Volume': volume_24h,
        'RSI': rsi,
        'SMA50': sma50,
        'SMA200': sma200,
        'EMA50': ema50,
        'EMA200': ema200,
        'VP_1d': vp_1d,
        'VP_7d': vp_7d,
        'VP_30d': vp_30d
    })

    model = load("C:\\Users\\arthu\\PycharmProjects\\Surchauffe_tools\\model\\btc_decision_tree_model.joblib")
    predictions = model.predict(df)
    return predictions

