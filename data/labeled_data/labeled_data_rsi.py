import data.calculated_data.rsi as rs


def labeled_rsi(coin_prices, offset=3):
    criteria_1 = 30
    criteria_2 = 70
    labels = []
    rsi = rs.rsi(coin_prices)  # On calcule le RSI pour tous les jours

    # On itère à travers les prix pour définir les labels
    for i in range(len(coin_prices) - offset):  # On prend en compte l'offset pour regarder dans le futur
        future_rsi = rsi[i + offset]  # RSI du jour futur

        # Si le RSI futur est supérieur à la barre supérieure, le label est 1 (forte tendance haussière)
        if future_rsi >= criteria_2:
            labels.append(1)
        # Si le RSI futur est entre les critères 1 et 2, le label est 0 (neutre)
        elif criteria_1 < future_rsi < criteria_2:
            labels.append(0)
        # Si le RSI futur est inférieur à la barre inférieure, le label est -1 (forte tendance baissière)
        else:
            labels.append(-1)

    # On complète avec des labels neutres pour les derniers jours, afin que la taille des labels soit identique à celle des prix
    labels.extend([0] * offset)

    return labels


