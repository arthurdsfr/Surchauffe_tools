import requests
import matplotlib.pyplot as plt
def fetch_eth_data(num_days):
    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {
        "vs_currency": "usd",
        "days": num_days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Extraire les dates et prix
        prices = data['prices']
        prices_value = [entry[1] for entry in prices]  # Prix en USD
        return prices_value
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return [], []

# Appel de la fonction
eth_prices = fetch_eth_data(365)



