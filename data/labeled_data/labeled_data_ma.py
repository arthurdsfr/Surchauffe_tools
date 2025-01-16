import data.calculated_data.moving_average as ma
import numpy as np
import matplotlib.pyplot as plt


def labeled_price_coin_sma50(coin_prices_365j):
    criteria_1 = 0.92
    criteria_2 = 1.08
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
    criteria_1 = 0.89
    criteria_2 = 1.11
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
    criteria_1 = 0.93
    criteria_2 = 1.11
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

