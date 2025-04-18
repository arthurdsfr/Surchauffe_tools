import requests

# Remplace par ta clé API Santiment


# URL de l'API pour obtenir les données sentimentales
url = f"https://api.santiment.net/v4/metrics/price:sentiment_score/?symbol=BTC&api_key=27cxwmomikn4rxk5_2rfig3l2atydye4a"

# Effectuer la requête
response = requests.get(url)

# Vérifier que la requête a bien réussi
if response.status_code == 200:
    data = response.json()
    # Afficher les premières données reçues
    print(data)
else:
    print(f"Erreur: {response.status_code}")
