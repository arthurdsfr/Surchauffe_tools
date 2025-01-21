import data.calculated_data.marketcap_avg as avg


def labeled_marketcap(coin_marketcap_365j):
    criteria_1 = 0.89 #critere + ou - 11%
    criteria_2 = 1.11
    labels = []
    marketcap_average = avg.average_marketcap(coin_marketcap_365j)
    for marketcap_1d in coin_marketcap_365j:
        if marketcap_1d >= marketcap_average * criteria_2:
            labels.append(1)
        elif marketcap_average * criteria_1 <= marketcap_1d < marketcap_average * criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels


