import data.labeled_data.labeled_data_marketcap as mc
import data.labeled_data.labeled_data_volume as vol
import data.labeled_data.labeled_data_rsi as rs
import data.labeled_data.labeled_variation_price as vp
import data.labeled_data.labeled_data_ma as ma
from data.recover_data.coin_from_dbeaver import *
from data.recover_data.coin_from_excel import *


def labelled_average(coin_price_365j, marketcap_365j, volume_24h_365j):
    number_variables = 10
    mc_labelled = mc.labeled_marketcap(marketcap_365j)
    vt_labelled = vol.labeled_volume(volume_24h_365j)
    rsi_labelled = rs.labeled_rsi(coin_price_365j)
    vp1d_labelled = vp.labeled_variation_price_1d(coin_price_365j)
    vp7d_labelled = vp.labeled_variation_price_7d(coin_price_365j)
    vp30d_labelled = vp.labeled_variation_price_30d(coin_price_365j)
    sma50_labelled = ma.labeled_price_coin_sma50(coin_price_365j)
    sma200_labelled = ma.labeled_price_coin_sma200(coin_price_365j)
    ema50_labelled = ma.labeled_price_coin_ema50(coin_price_365j)
    ema200_labelled = ma.labeled_price_coin_ema200(coin_price_365j)

    final_labels = []
    for i in range(len(coin_price_365j)):
        sum_labels = mc_labelled[i] + vt_labelled[i] + rsi_labelled[i] + vp1d_labelled[i] + vp7d_labelled[i] + vp30d_labelled[i] + sma50_labelled[i] + sma200_labelled[i] + ema50_labelled[i] + ema200_labelled[i]
        avg_labels = sum_labels / number_variables
        if avg_labels > 0.5:
            final_labels.append(1)
        elif -0.5 <= avg_labels <= 0.5:
            final_labels.append(0)
        else :
            final_labels.append(-1)
    return final_labels


def count_labels(labels):
    count_1 = labels.count(1)
    count_0 = labels.count(0)
    count_neg1 = labels.count(-1)
    return {"1": count_1, "0": count_0, "-1": count_neg1}


#coin_prices_60d, marketcap_60j, volume_24h = fetch_data_from_excel()
# # Utilisation de la fonction
# final_labels = labelled_average(coin_prices_60d, marketcap_60j, volume_24h)
# print(count_labels(final_labels))
