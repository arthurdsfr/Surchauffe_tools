def average_marketcap(coin_marketcap_365j):
    if len(coin_marketcap_365j) == 0:
        return None
    return sum(coin_marketcap_365j) / len(coin_marketcap_365j)