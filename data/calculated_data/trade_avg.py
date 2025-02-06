def average_trade(number_of_trades):
    if len(number_of_trades) == 0:
        return None
    return sum(number_of_trades) / len(number_of_trades)