import data.calculated_data.moving_average as ma
from data.recover_data.coin_from_excel import fetch_data_from_excel


def labeled_price_coin_sma50(coin_prices, offset=3):
    criteria_1 = 0.93
    criteria_2 = 1.07
    future_criteria_1 = 0.93
    future_criteria_2 = 1.07
    labels = []
    sma50 = ma.sma_50(coin_prices)

    for i in range(len(coin_prices)):
        if i + offset >= len(coin_prices):
            labels.append(None)  # Pas de données futures disponibles
            continue

        current_price = coin_prices[i]
        future_price = coin_prices[i + offset]
        sma_value = sma50[i]

        if current_price >= sma_value * criteria_2 and future_price >= sma_value * future_criteria_2:
            labels.append(1)
        elif (sma_value * criteria_1 < current_price < sma_value * criteria_2) and \
             (sma_value * future_criteria_1 < future_price < sma_value * future_criteria_2):
            labels.append(0)
        else:
            labels.append(-1)

    return labels



def labeled_price_coin_sma200(coin_prices, offset=3):
    criteria_1 = 0.90
    criteria_2 = 1.10
    future_criteria_1 = 0.90
    future_criteria_2 = 1.10
    labels = []
    sma200 = ma.sma_200(coin_prices)

    for i in range(len(coin_prices)):
        if i + offset >= len(coin_prices):
            labels.append(None)  # Pas de données futures disponibles
            continue

        current_price = coin_prices[i]
        future_price = coin_prices[i + offset]
        sma_value = sma200[i]

        if current_price >= sma_value * criteria_2 and future_price >= sma_value * future_criteria_2:
            labels.append(1)
        elif (sma_value * criteria_1 < current_price < sma_value * criteria_2) and \
             (sma_value * future_criteria_1 < future_price < sma_value * future_criteria_2):
            labels.append(0)
        else:
            labels.append(-1)

    return labels



def labeled_price_coin_ema50(coin_prices, offset=3):
    criteria_1 = 0.95
    criteria_2 = 1.05
    future_criteria_1 = 0.95
    future_criteria_2 = 1.05
    labels = []
    ema50 = ma.ema_50(coin_prices)

    for i in range(len(coin_prices)):
        if i + offset >= len(coin_prices):
            labels.append(None)  # Pas de données futures disponibles
            continue

        current_price = coin_prices[i]
        future_price = coin_prices[i + offset]
        ema_value = ema50[i]

        if current_price >= ema_value * criteria_2 and future_price >= ema_value * future_criteria_2:
            labels.append(1)
        elif (ema_value * criteria_1 < current_price < ema_value * criteria_2) and \
             (ema_value * future_criteria_1 < future_price < ema_value * future_criteria_2):
            labels.append(0)
        else:
            labels.append(-1)

    return labels



def labeled_price_coin_ema200(coin_prices, offset=3):
    criteria_1 = 0.94
    criteria_2 = 1.10
    future_criteria_1 = 0.94
    future_criteria_2 = 1.10
    labels = []

    ema200 = ma.ema_200(coin_prices)

    for i in range(len(coin_prices)):
        if i + offset >= len(coin_prices):
            labels.append(None)  # Pas de données futures disponibles
            continue

        current_price = coin_prices[i]
        future_price = coin_prices[i + offset]
        ema_value = ema200[i]

        # Logique combinée : actuel ET futur
        if current_price >= ema_value * criteria_2 and future_price >= ema_value * future_criteria_2:
            labels.append(1)
        elif (ema_value * criteria_1 < current_price < ema_value * criteria_2) and \
             (ema_value * future_criteria_1 < future_price < ema_value * future_criteria_2):
            labels.append(0)
        else:
            labels.append(-1)

    return labels