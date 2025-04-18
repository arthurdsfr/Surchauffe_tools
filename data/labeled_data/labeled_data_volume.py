import data.calculated_data.volume_trading_avg as ta
import data.calculated_data.variation_price as vp


def labeled_volume(coin_volume, coin_price, offset=3):
    criteria_1 = 0.75  # Critère -30%
    criteria_2 = 1.15  # Critère +20%
    labels = []
    volume_average = ta.volume_trading_average(coin_volume)
    prices_variation = vp.price_variation_1d(coin_price)

    # Ajouter un critère futur en utilisant un offset
    for i in range(len(coin_volume) - offset):
        future_price = coin_price[i + offset]  # Prix futur
        future_volume = coin_volume[i + offset]  # Volume futur
        price_var = prices_variation[i]  # Variation de prix actuelle

        # Critère basé sur le volume et la variation de prix actuelle
        if coin_volume[i] >= volume_average * criteria_2 and price_var > 0:
            labels.append(1)

        # Critère basé sur la comparaison du volume avec un critère et de la variation de prix actuelle
        elif volume_average * criteria_1 < coin_volume[i] < volume_average * criteria_2:
            labels.append(0)

        # Critère basé sur l'évolution future
        elif future_volume >= volume_average * criteria_2 and future_price > coin_price[i]:
            labels.append(1)  # Si le volume futur est élevé et que le prix augmente, tendance haussière

        # Autre condition en fonction de la baisse de prix et du volume
        elif future_volume < volume_average * criteria_1 and future_price < coin_price[i]:
            labels.append(-1)  # Si le volume futur est faible et que le prix baisse, tendance baissière

        else:
            labels.append(-1)  # Sinon, tendance baissière ou neutre

    # Compléter avec des labels neutres (0) pour les derniers éléments sans comparaison future
    labels.extend([0] * offset)

    return labels
