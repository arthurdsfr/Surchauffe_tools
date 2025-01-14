import data.calculated_data.variation_price as va
import numpy as np
def variation_price_1d_average(coin_price_365j):
    variation_price_1d_avg = va.price_variation_1d(coin_price_365j)
    if len(variation_price_1d_avg) == 0:
        return None
    return sum(variation_price_1d_avg) / len(variation_price_1d_avg)

def variation_price_7d_average(coin_price_365j):
    variation_price_7d_avg = va.price_variation_7d(coin_price_365j)
    if len(variation_price_7d_avg) == 0:
        return None
    return sum(variation_price_7d_avg) / len(variation_price_7d_avg)

def variation_price_30d_average(coin_price_365j):
    variation_price_30d_avg = va.price_variation_30d(coin_price_365j)
    if len(variation_price_30d_avg) == 0:
        return None
    return sum(variation_price_30d_avg) / len(variation_price_30d_avg)
