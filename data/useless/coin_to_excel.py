import requests
import pandas as pd

def fetch_eth_datas(num_days):
    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {
        "vs_currency": "usd",
        "days": num_days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        dates = [entry[0] for entry in data['prices']]
        prices = [entry[1] for entry in data['prices']]
        market_caps = [entry[1] / 10000000 for entry in data['market_caps']]
        volumes = [entry[1] / 10000000 for entry in data['total_volumes']]

        # Convertir les dates de timestamp UNIX à un format lisible
        dates = pd.to_datetime(dates, unit='ms')

        # Créer un DataFrame
        df = pd.DataFrame({
            'Date': dates,
            'Prix (USD)': prices,
            'MarketCap (USD)': market_caps,
            'Volume (USD)': volumes
        })

        return df
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return None
'''
# Récupérer les données sur les 365 derniers jours
eth_data_df = fetch_eth_datas(365)

if eth_data_df is not None:
    # Exporter les données vers un fichier Excel
    eth_data_df.to_excel('eth_data.xlsx', index=False)
    print("Les données ont été exportées avec succès vers 'eth_data.xlsx'.")
else:
    print("Aucune donnée à exporter.")
'''

def fetch_coin_datas(num_days):
    url = "https://api.coingecko.com/api/v3/coins/ankr/market_chart"
    params = {
        "vs_currency": "usd",
        "days": num_days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        dates = [entry[0] for entry in data['prices']]
        prices = [entry[1] for entry in data['prices']]
        market_caps = [entry[1] / 1000000 for entry in data['market_caps']]
        volumes = [entry[1] / 1000000 for entry in data['total_volumes']]

        # Convertir les dates de timestamp UNIX à un format lisible
        dates = pd.to_datetime(dates, unit='ms')

        # Créer un DataFrame
        df = pd.DataFrame({
            'Date': dates,
            'Prix (USD)': prices,
            'MarketCap (USD)': market_caps,
            'Volume (USD)': volumes
        })

        return df
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return None

# # Récupérer les données sur les 365 derniers jours
# coin_data_df = fetch_coin_datas(365)
#
# if coin_data_df is not None:
#     # Exporter les données vers un fichier Excel
#     coin_data_df.to_excel('ankr_data.xlsx', index=False)
#     print("Les données ont été exportées avec succès")
# else:
#     print("Aucune donnée à exporter.")


