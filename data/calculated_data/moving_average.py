import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ema_50(coin_prices_365j):
    serie_price = pd.Series(coin_prices_365j)
    list_ema_50 = serie_price.ewm(span=50, adjust=False).mean()
    return list_ema_50

def sma_50(coin_prices_365j):
    serie_price = pd.Series(coin_prices_365j)
    list_ma_50 = serie_price.rolling(window=50, min_periods=1).mean()
    return list_ma_50

def ema_200(coin_prices_365j):
    serie_price = pd.Series(coin_prices_365j)
    list_ema_200 = serie_price.ewm(span=200, adjust=False).mean()
    return list_ema_200

def sma_200(coin_prices_365j):
    serie_price = pd.Series(coin_prices_365j)
    list_ma_200 = serie_price.rolling(window=200, min_periods=1).mean()
    return list_ma_200

np.random.seed(42)  # Pour la reproductibilité
jours = 365
prix_initial = 100
# Générer des variations journalières avec une moyenne de 0 et une écart-type de 2
variations = np.random.normal(0, 2, jours)
# Calculer les prix en cumulant les variations
prix = prix_initial + np.cumsum(variations)


plt.figure(figsize=(14, 7))
plt.plot(prix, label='Prix simulés', color='blue', alpha=0.6)
plt.plot(sma_50(prix), label='SMA 50 jours', color='orange', linestyle='--')
plt.plot(ema_50(prix), label='EMA 50 jours', color='green', linestyle='--')
plt.plot(sma_200(prix), label='SMA 200 jours', color='red', linestyle='--')
plt.plot(ema_200(prix), label='EMA 200 jours', color='black', linestyle='--')
plt.title('Prix simulés avec SMA et EMA sur 50 jours')
plt.xlabel('Jours')
plt.ylabel('Prix')
plt.legend()
plt.grid(True)
#plt.savefig('test_ema_sma')