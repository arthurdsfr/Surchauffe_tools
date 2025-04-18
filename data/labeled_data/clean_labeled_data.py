import data.labeled_data.labeled_data_volume as vol
import data.labeled_data.labeled_data_rsi as rs
import data.labeled_data.labeled_variation_price as vp
import data.labeled_data.labeled_data_ma as ma
import data.labeled_data.labeled_data_trade as tr
from data.recover_data.coin_from_excel import fetch_data_from_excel


def labelled_average(coin_prices, number_trade, volumes_24h):
    number_variables = 10
    tr_labelled = tr.labeled_trade(number_trade, coin_prices)
    vt_labelled = vol.labeled_volume(volumes_24h, coin_prices)
    rsi_labelled = rs.labeled_rsi(coin_prices)
    vp1d_labelled = vp.labeled_variation_price_1d(coin_prices)
    vp7d_labelled = vp.labeled_variation_price_7d(coin_prices)
    vp30d_labelled = vp.labeled_variation_price_30d(coin_prices)
    sma50_labelled = ma.labeled_price_coin_sma50(coin_prices)
    sma200_labelled = ma.labeled_price_coin_sma200(coin_prices)
    ema50_labelled = ma.labeled_price_coin_ema50(coin_prices)
    ema200_labelled = ma.labeled_price_coin_ema200(coin_prices)

    final_labels = []

    for i in range(len(coin_prices)):
        # Vérification de chaque label pour s'assurer qu'il n'est pas None
        labels = [
            tr_labelled[i], vt_labelled[i], rsi_labelled[i], vp1d_labelled[i],
            vp7d_labelled[i], vp30d_labelled[i], sma50_labelled[i], sma200_labelled[i],
            ema50_labelled[i], ema200_labelled[i]
        ]

        # Si l'un des labels est None, on le remplace par 0 (ou un autre comportement souhaité)
        if any(label is None for label in labels):
            sum_labels = 0  # On ignore cet élément, ou on peut ajuster en fonction de votre logique
        else:
            sum_labels = sum(labels)

        # Calcul du label final basé sur la somme des labels
        avg_labels = sum_labels / number_variables
        if avg_labels > 0.4:
            final_labels.append(1)
        elif -0.4 <= avg_labels <= 0.4:
            final_labels.append(0)
        else:
            final_labels.append(-1)

    return final_labels


def count_labels(labels):
    count_1 = labels.count(1)
    count_0 = labels.count(0)
    count_neg1 = labels.count(-1)
    return {"1": count_1, "0": count_0, "-1": count_neg1}


# import matplotlib.pyplot as plt
#
#
# def plot_price_and_labels(coin_prices, final_labels):
#     fig, axs = plt.subplots(2, 1, figsize=(14, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
#
#     # Graphique 1 : Courbe du prix du Bitcoin
#     axs[0].plot(coin_prices, label='Prix du BTC', color='blue')
#     axs[0].set_title('Évolution du prix du Bitcoin')
#     axs[0].set_ylabel('Prix (USD)')
#     axs[0].grid(True)
#     axs[0].legend()
#
#     # Graphique 2 : Labels (-1, 0, 1)
#     axs[1].plot(final_labels, label='Labels de classification', color='orange', marker='o', linestyle='-')
#     axs[1].set_title('Labels (baisse = -1, neutre = 0, hausse = 1)')
#     axs[1].set_xlabel('Temps (jours)')
#     axs[1].set_yticks([-1, 0, 1])
#     axs[1].set_ylabel('Label')
#     axs[1].grid(True)
#     axs[1].legend()
#
#     plt.tight_layout()
#     plt.show()
#
# df, coin_prices_60d, marketcap_60j, volume_24h = fetch_data_from_excel()
# # Utilisation de la fonction
# final_labels = labelled_average(coin_prices_60d, marketcap_60j, volume_24h)
# print(count_labels(final_labels))
# plot_price_and_labels(coin_prices_60d, final_labels)
