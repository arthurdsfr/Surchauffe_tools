import requests
import matplotlib.pyplot as plt

def fetch_eth_datas(num_days):
    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {
        "vs_currency": "usd",
        "days": num_days,
        "interval": "daily",
        "price_change_percentage": "7d,30d"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        prices_value = [entry[1] for entry in data['prices']]  # On récupère uniquement les prix en USD
        market_cap_value = [entry[1] for entry in data['market_caps']]
        volume_trading_24h_value = [entry[1] for entry in data['total_volumes']]
        return prices_value, market_cap_value, volume_trading_24h_value
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return []

# Récupérer les prix de l'Ethereum sur les 365 derniers jours
#eth_prices, market_cap, volume_trading_24h = fetch_eth_datas(365)


#print(len(eth_prices))
#print(len(market_cap))
#print(len(volume_trading_24h))

# Tracer le graphique
#plt.figure(figsize=(10, 5))
#plt.plot(eth_prices, label="Prix de l'Ethereum (USD)", color="blue")
#plt.title("Évolution du prix de l'Ethereum sur les 365 derniers jours")
#plt.xlabel("Jour")
#plt.ylabel("Prix en USD")
#plt.legend()
#plt.grid(True)
#plt.savefig('graph_eth_price')



