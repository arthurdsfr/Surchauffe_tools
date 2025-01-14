import numpy as np

def price_variation_1d(coin_prices_365j):
    price_variation_1d = [0]
    for day in range(1, len(coin_prices_365j)):
        ecart = coin_prices_365j[day] - coin_prices_365j[day-1]
        ecart_percentage = (ecart/coin_prices_365j[day-1])*100
        price_variation_1d.append(ecart_percentage)
    return price_variation_1d

def price_variation_7d(coin_prices_365j):
    price_variation_7d = [0]
    for day in range(1, 7):
        ecart = coin_prices_365j[day] - coin_prices_365j[0]
        ecart_percentage = (ecart/coin_prices_365j[0])*100
        price_variation_7d.append(ecart_percentage)
    for day in range(7, len(coin_prices_365j)):
        ecart = coin_prices_365j[day] - coin_prices_365j[day-7]
        ecart_percentage = (ecart/coin_prices_365j[day-7])*100
        price_variation_7d.append(ecart_percentage)

    return price_variation_7d

def price_variation_30d(coin_prices_365j):
    price_variation_30d = [0]
    for day in range(1, 30):
        ecart = coin_prices_365j[day] - coin_prices_365j[0]
        ecart_percentage = (ecart/coin_prices_365j[0])*100
        price_variation_30d.append(ecart_percentage)
    for day in range(30, len(coin_prices_365j)):
        ecart = coin_prices_365j[day] - coin_prices_365j[day-30]
        ecart_percentage = (ecart/coin_prices_365j[day-30])*100
        price_variation_30d.append(ecart_percentage)

    return price_variation_30d



