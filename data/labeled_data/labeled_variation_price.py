import data.calculated_data.variation_price as vp


def labeled_variation_price_1d(coin_prices, offset=3):
    criteria_1d = 4  # Critère de variation de prix de +/- 5%
    labels = []
    vp_1d = vp.price_variation_1d(coin_prices)

    # Ajouter un critère futur basé sur les variations de prix
    for i in range(len(coin_prices) - offset):
        future_variation_price = vp_1d[i + offset]  # Variation de prix future
        variation_price = vp_1d[i]  # Variation de prix actuelle

        # Critère basé sur la variation de prix actuelle
        if variation_price >= criteria_1d:
            labels.append(1)

        # Critère basé sur une variation de prix actuelle proche de 0
        elif -criteria_1d < variation_price < criteria_1d:
            labels.append(0)

        # Critère basé sur la variation de prix future
        elif future_variation_price >= criteria_1d:
            labels.append(1)  # Si la variation future est positive et supérieure à 5%, tendance haussière

        elif future_variation_price <= -criteria_1d:
            labels.append(-1)  # Si la variation future est négative et inférieure à -5%, tendance baissière

        else:
            labels.append(-1)  # Si aucune condition spécifique n'est remplie, tendance baissière

    # Compléter avec des labels neutres (0) pour les derniers éléments sans comparaison future
    labels.extend([0] * offset)

    return labels


def labeled_variation_price_7d(coin_prices, offset=3):
    criteria_7d = 8  # Critère de variation de prix de +/- 10%
    labels = []
    vp_7d = vp.price_variation_7d(coin_prices)

    # Ajouter un critère futur basé sur les variations de prix sur 7 jours
    for i in range(len(coin_prices) - offset):
        future_variation_price_7d = vp_7d[i + offset]  # Variation de prix sur 7 jours dans le futur
        variation_price_7d = vp_7d[i]  # Variation de prix sur 7 jours actuelle

        # Critère basé sur la variation de prix actuelle
        if variation_price_7d >= criteria_7d:
            labels.append(1)

        # Critère basé sur une variation de prix actuelle proche de 0
        elif -criteria_7d < variation_price_7d < criteria_7d:
            labels.append(0)

        # Critère basé sur la variation de prix future
        elif future_variation_price_7d >= criteria_7d:
            labels.append(1)  # Si la variation future est positive et supérieure à 10%, tendance haussière

        elif future_variation_price_7d <= -criteria_7d:
            labels.append(-1)  # Si la variation future est négative et inférieure à -10%, tendance baissière

        else:
            labels.append(-1)  # Si aucune condition spécifique n'est remplie, tendance baissière

    # Compléter avec des labels neutres (0) pour les derniers éléments sans comparaison future
    labels.extend([0] * offset)

    return labels


def labeled_variation_price_30d(coin_prices, offset=3):
    criteria_30d = 5  # Critère de variation de prix de +/- 5%
    labels = []
    vp_30d = vp.price_variation_30d(coin_prices)

    # Ajouter un critère futur basé sur les variations de prix sur 30 jours
    for i in range(len(coin_prices) - offset):
        future_variation_price_30d = vp_30d[i + offset]  # Variation de prix sur 30 jours dans le futur
        variation_price_30d = vp_30d[i]  # Variation de prix sur 30 jours actuelle

        # Critère basé sur la variation de prix actuelle
        if variation_price_30d >= criteria_30d:
            labels.append(1)

        # Critère basé sur une variation de prix actuelle proche de 0
        elif -criteria_30d < variation_price_30d < criteria_30d:
            labels.append(0)

        # Critère basé sur la variation de prix future
        elif future_variation_price_30d >= criteria_30d:
            labels.append(1)  # Si la variation future est positive et supérieure à 5%, tendance haussière

        elif future_variation_price_30d <= -criteria_30d:
            labels.append(-1)  # Si la variation future est négative et inférieure à -5%, tendance baissière

        else:
            labels.append(-1)  # Si aucune condition spécifique n'est remplie, tendance baissière

    # Compléter avec des labels neutres (0) pour les derniers éléments sans comparaison future
    labels.extend([0] * offset)

    return labels


