import data.calculated_data.volume_trading_avg as ta


def labeled_volume(coin_volume_365j):
    criteria_1 = 0.7
    criteria_2 = 1.20
    labels = []
    volume_average = ta.volume_trading_average(coin_volume_365j)
    for volume_1d in coin_volume_365j:
        if volume_1d >= volume_average*criteria_2:
            labels.append(1)
        elif volume_average*criteria_1 < volume_1d < volume_average*criteria_2:
            labels.append(0)
        else :
            labels.append(-1)
    return labels
