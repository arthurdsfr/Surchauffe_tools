import data.calculated_data.volume_trading_avg as ta
import data.calculated_data.variation_price as vp

def labeled_volume(coin_volume, coin_price):
    criteria_1 = 0.7
    criteria_2 = 1.20
    labels = []
    volume_average = ta.volume_trading_average(coin_volume)
    for volume_1d, price in zip(coin_volume, coin_price):
            if volume_1d >= volume_average*criteria_2 and vp.price_variation_1d(price) > 0:
                labels.append(1)
            elif volume_average*criteria_1 < volume_1d < volume_average*criteria_2:
                labels.append(0)
            else :
                labels.append(-1)
    return labels
