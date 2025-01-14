import data.calculated_data.marketcap_average as avg
import numpy as np

def labeled_marketcap(coin_marketcap_365j):
    criteria_1 = 0.7 #critere + ou - 30%
    criteria_2 = 1.3
    labels = []
    marketcap_average = avg.average_marketcap(coin_marketcap_365j)
    for marketcap_1d in coin_marketcap_365j:
        if marketcap_1d >= marketcap_average*criteria_2:
            labels.append(1)
        elif marketcap_1d*criteria_1 < marketcap_1d < marketcap_average*criteria_2:
            labels.append(0)
        else :
            labels.append(-1)
    return labels


def compter_occurrences(liste):
    count_1 = liste.count(1)
    count_0 = liste.count(0)
    count_neg1 = liste.count(-1)
    return count_1, count_0, count_neg1

np.random.seed(42)  # Pour la reproductibilité
jours = 365
prix_initial = 100
# Générer des variations journalières avec une moyenne de 0 et une écart-type de 2
variations = np.random.normal(0, 2, jours)
# Calculer les prix en cumulant les variations
prix = prix_initial + np.cumsum(variations)


labeled = labeled_marketcap(prix)
count_1, count_0, count_neg1 = compter_occurrences(labeled)

print(len(labeled))
print(f"Nombre de 1 : {count_1}")
print(f"Nombre de 0 : {count_0}")
print(f"Nombre de -1 : {count_neg1}")



