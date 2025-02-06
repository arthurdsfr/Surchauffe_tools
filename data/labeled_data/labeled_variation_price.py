import data.calculated_data.variation_price as vp

def labeled_variation_price_1d(coin_prices):
    criteria_1d = 5
    labels = []
    vp_1d = vp.price_variation_1d(coin_prices)
    for variation_price in vp_1d:
        if variation_price >= criteria_1d:
            labels.append(1)
        elif -criteria_1d < variation_price < criteria_1d:
            labels.append(0)
        else :
            labels.append(-1)
    return labels

def labeled_variation_price_7d(coin_prices):
    criteria_1d = 10
    labels = []
    vp_7d = vp.price_variation_7d(coin_prices)
    for variation_price in vp_7d:
        if variation_price >= criteria_1d:
            labels.append(1)
        elif -criteria_1d < variation_price < criteria_1d:
            labels.append(0)
        else :
            labels.append(-1)
    return labels

def labeled_variation_price_30d(coin_prices):
    criteria_30d = 5
    labels = []
    vp_1d = vp.price_variation_1d(coin_prices)
    for variation_price in vp_1d:
        if variation_price >= criteria_30d:
            labels.append(1)
        elif -criteria_30d < variation_price < criteria_30d:
            labels.append(0)
        else :
            labels.append(-1)
    return labels

