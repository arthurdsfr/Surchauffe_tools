import requests

def fetch_altcoins_data(altcoins, num_days):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    all_data = []
    params = {
        "vs_currency": "usd",
        "ids": ",".join(altcoins),
        "order": "market_cap_desc",
        "days": num_days,
        "interval": "daily",
        "price_change_percentage": "7d,30d"
        }
    response = requests.get(url, params=params)
    data = response.json()
    all_data.extend(data) #extend because adding each value separately

    return all_data

altcoins = ['bitcoin', 'ethereum']
data = fetch_altcoins_data(altcoins,500)

# Afficher les données récupérées pour chaque altcoin

for coin in data:
    if isinstance(coin, dict):  # Vérifie que coin est un dictionnaire
        print(f"{coin['name']} ({coin['symbol'].upper()}):")
        print(f"  Price: {coin['current_price']} USD")
        print(f"  Volume 24h: {coin['total_volume']} USD")
        print(f"  Price change 24h: {coin['price_change_percentage_24h']}%")
        print()