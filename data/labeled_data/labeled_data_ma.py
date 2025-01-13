import data.calculated_data.mobile_average as ma
import numpy as np
import matplotlib.pyplot as plt

def compter_occurrences(liste):
    count_1 = liste.count(1)
    count_0 = liste.count(0)
    count_neg1 = liste.count(-1)
    return count_1, count_0, count_neg1

def labeled_price_coin_sma50(coin_prices_365j):
    criteria_1 = 0.90
    criteria_2 = 1.10
    labels = []
    sma50 = ma.sma_50(coin_prices_365j)
    for i in range(0, len(coin_prices_365j)):
        if coin_prices_365j[i] >= sma50[i]*criteria_2:
            labels.append(1)
        elif sma50[i]*criteria_1 < coin_prices_365j[i] < sma50[i]*criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels

def labeled_price_coin_sma200(coin_prices_365j):
    criteria_1 = 0.92
    criteria_2 = 1.08
    labels = []
    sma200 = ma.sma_200(coin_prices_365j)
    for i in range(0, len(coin_prices_365j)):
        if coin_prices_365j[i] >= sma200[i]*criteria_2:
            labels.append(1)
        elif sma200[i]*criteria_1 < coin_prices_365j[i] < sma200[i]*criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels

def labeled_price_coin_ema50(coin_prices_365j):
    criteria_1 = 0.95
    criteria_2 = 1.05
    labels = []
    ema50 = ma.ema_50(coin_prices_365j)
    for i in range(0, len(coin_prices_365j)):
        if coin_prices_365j[i] >= ema50[i]*criteria_2:
            labels.append(1)
        elif ema50[i]*criteria_1 < coin_prices_365j[i] < ema50[i]*criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels
def labeled_price_coin_ema200(coin_prices_365j):
    criteria_1 = 0.92
    criteria_2 = 1.08
    labels = []
    ema200 = ma.ema_200(coin_prices_365j)
    for i in range(0, len(coin_prices_365j)):
        if coin_prices_365j[i] >= ema200[i]*criteria_2:
            labels.append(1)
        elif ema200[i]*criteria_1 < coin_prices_365j[i] < ema200[i]*criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels

np.random.seed(42)  # Pour la reproductibilité
jours = 365
prix_initial = 100
# Générer des variations journalières avec une moyenne de 0 et une écart-type de 2
variations = np.random.normal(0, 2, jours)
# Calculer les prix en cumulant les variations
prix = prix_initial + np.cumsum(variations)


labeled = labeled_price_coin_ema200(prix)
count_1, count_0, count_neg1 = compter_occurrences(labeled)

print(len(labeled))
print(f"Nombre de 1 : {count_1}")
print(f"Nombre de 0 : {count_0}")
print(f"Nombre de -1 : {count_neg1}")


plt.figure(figsize=(14, 7))
plt.plot(prix, label='Prix simulés', color='blue', alpha=0.6)
plt.plot(ma.ema_200(prix), label='SMA 50 jours', color='orange', linestyle='--')
plt.grid(True)
plt.savefig('test_ema_sma')