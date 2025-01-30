import data.calculated_data.rsi as rs
import data.calculated_data.moving_average as ma
import data.calculated_data.variation_price as vp
from data.recover_data.coin_from_dbeaver import *
from data.recover_data.coin_from_excel import *
import pandas as pd
from joblib import load

# Fonction pour faire des prédictions
def predict_model(coin_prices_365j, marketcap_365j, volume_24h_365j):
    # Calculer les mêmes caractéristiques que pendant l'entraînement
    rsi = rs.rsi(coin_prices_365j)
    sma50 = ma.sma_50(coin_prices_365j)
    sma200 = ma.sma_200(coin_prices_365j)
    ema50 = ma.ema_50(coin_prices_365j)
    ema200 = ma.ema_200(coin_prices_365j)
    vp_1d = vp.price_variation_1d(coin_prices_365j)
    vp_7d = vp.price_variation_7d(coin_prices_365j)
    vp_30d = vp.price_variation_30d(coin_prices_365j)

    # Créer le DataFrame avec les caractéristiques calculées
    df = pd.DataFrame({
        'Price': coin_prices_365j,
        'Market Cap': marketcap_365j,
        'Volume': volume_24h_365j,
        'RSI': rsi,
        'SMA50': sma50,
        'SMA200': sma200,
        'EMA50': ema50,
        'EMA200': ema200,
        'VP_1d': vp_1d,
        'VP_7d': vp_7d,
        'VP_30d': vp_30d
    })

    model = load("C:\\Users\\arthu\\PycharmProjects\\Surchauffe_tools\\model\\solana_decision_tree_model.joblib")
    prediction = model.predict(df)
    return prediction


# coin_prices_60d, marketcap_60j, volume_24h = fetch_60d_from_excel()
# prediction = predict_model(coin_prices_60d, marketcap_60j, volume_24h)
# print(prediction)

