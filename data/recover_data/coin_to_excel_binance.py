import requests
import pandas as pd

def get_historical_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        'symbol': "BTCUSDT",
        'interval': "1d",
        'limit': 60  # Max 1000 bougies par requête
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=[
            "Open Time", "Open", "High", "Low", "Close", "Volume",
            "Close Time", "Quote Asset Volume", "Number of Trades",
            "Taker Buy Base Volume", "Taker Buy Quote Volume", "Ignore"
        ])
        df_data = df[["Close", "Volume", "Number of Trades"]]
        return df_data
    else :
        print("Erreur API Binance")
        return None

df_data = get_historical_data()
df_data.to_excel("BTC_test.xlsx")


