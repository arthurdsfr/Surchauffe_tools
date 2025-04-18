
def price_variation_1d(coin_prices):
    price_variation_1d = [0]
    for day in range(1, len(coin_prices)):
        ecart = coin_prices[day] - coin_prices[day-1]
        ecart_percentage = (ecart/coin_prices[day-1])*100
        price_variation_1d.append(ecart_percentage)
    return price_variation_1d


def price_variation_7d(coin_prices):
    if len(coin_prices) < 7:
        raise ValueError("La liste coin_prices_365j doit contenir au moins 7 éléments.")

    price_variation_7d = [0]

    # Calcul des variations pour les 7 premiers jours
    for day in range(1, 7):
        ecart = coin_prices[day] - coin_prices[0]
        ecart_percentage = (ecart / coin_prices[0]) * 100
        price_variation_7d.append(ecart_percentage)

    # Calcul des variations au-delà des 7 jours
    for day in range(7, len(coin_prices)):
        ecart = coin_prices[day] - coin_prices[day - 7]
        ecart_percentage = (ecart / coin_prices[day - 7]) * 100
        price_variation_7d.append(ecart_percentage)

    return price_variation_7d


def price_variation_30d(coin_prices):
    if len(coin_prices) < 30:
        raise ValueError("La liste coin_prices_365j doit contenir au moins 30 éléments.")

    price_variation_30d = [0]
    for day in range(1, 30):
        ecart = coin_prices[day] - coin_prices[0]
        ecart_percentage = (ecart/coin_prices[0])*100
        price_variation_30d.append(ecart_percentage)
    for day in range(30, len(coin_prices)):
        ecart = coin_prices[day] - coin_prices[day-30]
        ecart_percentage = (ecart/coin_prices[day-30])*100
        price_variation_30d.append(ecart_percentage)

    return price_variation_30d



