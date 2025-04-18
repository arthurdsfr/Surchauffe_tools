import data.calculated_data.trade_avg as avg
import data.calculated_data.variation_price as vp


def labeled_trade(number_of_trades, coin_prices, offset=3):
    criteria_1 = 0.90  # critère + ou - 11%
    criteria_2 = 1.10
    labels = []

    # Calcul de la moyenne des trades sur la période
    trade_average = avg.average_trade(number_of_trades)
    prices_variation = vp.price_variation_1d(coin_prices)

    # On itère à travers les données pour définir les labels
    for i in range(len(number_of_trades) - offset):
        # On récupère les valeurs futures pour le nombre de trades et la variation des prix
        future_trade = number_of_trades[i + offset]
        future_price_var = prices_variation[i + offset]

        # On applique la même logique pour les labels en fonction des critères
        if future_trade >= trade_average * criteria_2 and future_price_var > 0:
            labels.append(1)
        elif trade_average * criteria_1 <= future_trade < trade_average * criteria_2:
            labels.append(0)
        else:
            labels.append(-1)

    # On ajoute des labels neutres pour les derniers jours afin de maintenir la taille des labels
    labels.extend([0] * offset)

    return labels



