import requests
import matplotlib.pyplot as plt

def fetch_eth_prices(num_days):
    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {
        "vs_currency": "usd",
        "days": num_days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        prices = data['prices']  # Liste des [timestamp, prix]
        prices_value = [entry[1] for entry in prices]  # On récupère uniquement les prix en USD
        return prices_value
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return []

# Récupérer les prix de l'Ethereum sur les 365 derniers jours
eth_prices = fetch_eth_prices(365)

# Tracer le graphique
plt.figure(figsize=(10, 5))
plt.plot(eth_prices, label="Prix de l'Ethereum (USD)", color="blue")
plt.title("Évolution du prix de l'Ethereum sur les 365 derniers jours")
plt.xlabel("Jour")
plt.ylabel("Prix en USD")
plt.legend()
plt.grid(True)
plt.savefig('graph_eth_price')



