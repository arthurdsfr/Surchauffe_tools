def volume_trading_average(coin_volume_365j):
    if len(coin_volume_365j) == 0:
        return None
    return sum(coin_volume_365j) / len(coin_volume_365j)

