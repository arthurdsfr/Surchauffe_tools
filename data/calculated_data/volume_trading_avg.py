def volume_trading_average(coin_volume):
    if len(coin_volume) == 0:
        return None
    return sum(coin_volume) / len(coin_volume)

