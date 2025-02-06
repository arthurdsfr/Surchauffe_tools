import data.calculated_data.trade_avg as avg
import data.calculated_data.variation_price as vp

def labeled_trade(number_of_trades, coin_prices):
    criteria_1 = 0.89 #critere + ou - 11%
    criteria_2 = 1.11
    labels = []
    trade_average = avg.average_trade(number_of_trades)
    for trade_1d, prices in zip(number_of_trades, coin_prices):
        if trade_1d >= trade_average * criteria_2 and vp.price_variation_1d(prices) > 0:
            labels.append(1)
        elif trade_average * criteria_1 <= trade_1d < trade_average * criteria_2:
            labels.append(0)
        else:
            labels.append(-1)
    return labels


