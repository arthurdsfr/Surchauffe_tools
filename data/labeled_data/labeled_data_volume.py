import data.calculated_data.volume_trading_avg as ta
import data.calculated_data.variation_price as vp

def labeled_volume(coin_volume, coin_price):
    criteria_1 = 0.7
    criteria_2 = 1.20
    labels = []
    volume_average = ta.volume_trading_average(coin_volume)
    prices_variation = vp.price_variation_1d(coin_price)
    for volume_1d, price_var in zip(coin_volume, prices_variation):
            if volume_1d >= volume_average*criteria_2 and price_var > 0:
                labels.append(1)
            elif volume_average*criteria_1 < volume_1d < volume_average*criteria_2:
                labels.append(0)
            else :
                labels.append(-1)
    return labels
