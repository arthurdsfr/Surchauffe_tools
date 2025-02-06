from data.recover_data.coin_from_excel import *
import data.labeled_data.clean_labeled_data as clean
import data.calculated_data.rsi as rs
import data.calculated_data.moving_average as ma
import data.calculated_data.variation_price as vp
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

def train_model(coin_prices, number_trades, volume_24h):
    rsi = rs.rsi(coin_prices)
    sma50 = ma.sma_50(coin_prices)
    sma200 = ma.sma_200(coin_prices)
    ema50 = ma.ema_50(coin_prices)
    ema200 = ma.ema_200(coin_prices)
    vp_1d = vp.price_variation_1d(coin_prices)
    vp_7d = vp.price_variation_7d(coin_prices)
    vp_30d = vp.price_variation_30d(coin_prices)
    labels = clean.labelled_average(coin_prices, number_trades, volume_24h)

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
        'VP_30d': vp_30d,
        'Labels': labels
    })

    X = df.drop(columns=['Labels'])
    y = df['Labels']

    X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train, Y_train)
    dump(decision_tree, 'btc_decision_tree_model.joblib')
    print("Modèle sauvegardé sous le nom : 'btc_decision_tree_model.joblib'")
    test_tree = decision_tree.score(x_test, y_test)
    return test_tree

# df, coin_prices, number_trades, volume_24h = fetch_data_from_excel()
# test_tree = train_model(coin_prices, number_trades, volume_24h)
# print(test_tree)









