import labeled_data_marketcap
import labeled_data_volume
import labeled_data_rsi
import labeled_variation_price
import labeled_data_ma
import data.recover_data.eth_from_excel as excel

def labelled_average(coin_price_365j, marketcap_365j, volume_24h_365j):
    number_variables = 10
    mc_labelled = labeled_data_marketcap.labeled_marketcap(marketcap_365j)
    vt_labelled = labeled_data_volume.labeled_volume(volume_24h_365j)
    rsi_labelled = labeled_data_rsi.labeled_rsi(coin_price_365j)
    vp1d_labelled = labeled_variation_price.labeled_variation_price_1d(coin_price_365j)
    vp7d_labelled = labeled_variation_price.labeled_variation_price_7d(coin_price_365j)
    vp30d_labelled = labeled_variation_price.labeled_variation_price_30d(coin_price_365j)
    sma50_labelled = labeled_data_ma.labeled_price_coin_sma50(coin_price_365j)
    sma200_labelled = labeled_data_ma.labeled_price_coin_sma200(coin_price_365j)
    ema50_labelled = labeled_data_ma.labeled_price_coin_ema50(coin_price_365j)
    ema200_labelled = labeled_data_ma.labeled_price_coin_ema200(coin_price_365j)

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


eth_prices_365j, marketcap_365j, volume_24h_365j = excel.fetch_eth_data_from_excel()
