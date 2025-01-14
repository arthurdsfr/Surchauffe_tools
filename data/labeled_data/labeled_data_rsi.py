import data.calculated_data.rsi as rs
import numpy as np

def labeled_rsi(coin_prices_365j):
    criteria_1 = 30
    criteria_2 = 70
    labels = []
    rsi = rs.rsi(coin_prices_365j)
    for rsi_1d in rsi:
        if rsi_1d >= criteria_2:
            labels.append(1)
        elif criteria_1 < rsi_1d < criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels