
def price_variation_1d(eth_prices_365j):
    price_variation_1d = [0]
    for day in range(1, len(eth_prices_365j)):
        ecart = eth_prices_365j[day] - eth_prices_365j[day-1]
        ecart_percentage = (ecart/eth_prices_365j[day-1])*100
        price_variation_1d.append(ecart_percentage)

    return price_variation_1d

def price_variation_7d(eth_prices_365j):
    price_variation_7d = [0]
    for day in range(1, 7):
        ecart = eth_prices_365j[day] - eth_prices_365j[0]
        ecart_percentage = (ecart/eth_prices_365j[0])*100
        price_variation_7d.append(ecart_percentage)
    for day in range(7, len(eth_prices_365j)):
        ecart = eth_prices_365j[day] - eth_prices_365j[day-7]
        ecart_percentage = (ecart/eth_prices_365j[day-7])*100
        price_variation_7d.append(ecart_percentage)

    return price_variation_7d

def price_variation_30d(eth_prices_365j):
    price_variation_30d = [0]
    for day in range(1, 30):
        ecart = eth_prices_365j[day] - eth_prices_365j[0]
        ecart_percentage = (ecart/eth_prices_365j[0])*100
        price_variation_30d.append(ecart_percentage)
    for day in range(30, len(eth_prices_365j)):
        ecart = eth_prices_365j[day] - eth_prices_365j[day-30]
        ecart_percentage = (ecart/eth_prices_365j[day-30])*100
        price_variation_30d.append(ecart_percentage)

    return price_variation_30d
