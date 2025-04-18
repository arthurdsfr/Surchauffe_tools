import numpy as np
import matplotlib.pyplot as plt
import data.calculated_data.rsi as rs
import data.calculated_data.moving_average as ma
import data.calculated_data.variation_price as vp

def plot_indicators(df, coin_prices):
    dates = np.arange(len(df))  # Création d'un axe temporel fictif

    fig, axs = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

    # Prix et Moyennes Mobiles
    axs[0].plot(dates, df['Close'], label="Price", color='black')
    axs[0].plot(dates, ma.sma_50(coin_prices), label="SMA50", linestyle="dashed", color='blue')
    axs[0].plot(dates, ma.sma_200(coin_prices), label="SMA200", linestyle="dashed", color='red')
    axs[0].set_title("Prix et Moyennes Mobiles")
    axs[0].legend()

    # RSI
    axs[1].plot(dates, rs.rsi(coin_prices), label="RSI", color='purple')
    axs[1].axhline(y=70, color='r', linestyle='dashed', label="Surachat (70)")
    axs[1].axhline(y=30, color='g', linestyle='dashed', label="Survente (30)")
    axs[1].set_title("RSI")
    axs[1].legend()

    # Variation du prix
    axs[2].plot(dates, vp.price_variation_1d(coin_prices), label="VP_1d", color='orange')
    axs[2].plot(dates, vp.price_variation_7d(coin_prices), label="VP_7d", color='blue')
    axs[2].plot(dates, vp.price_variation_30d(coin_prices), label="VP_30d", color='red')
    axs[2].set_title("Variation du Prix")
    axs[2].legend()

    plt.xlabel("Jours")
    plt.tight_layout()
    plt.show()

def plot_results(df, predictions, coin_prices):
    dates = np.arange(len(df))  # Création d'un axe temporel fictif

    fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)  # Création de deux sous-graphes (subplot)

    # Tracer le prix du Bitcoin
    axs[0].plot(dates, coin_prices, label="Prix du Bitcoin", color='black')
    axs[0].set_title("Prix du Bitcoin")
    axs[0].set_ylabel("Prix")
    axs[0].legend()

    # Tracer les prédictions du modèle
    axs[1].plot(dates, predictions, label="Prédictions", marker='o', color='green')
    axs[1].set_title("Prédictions du Modèle")
    axs[1].set_xlabel("Dates")
    axs[1].set_ylabel("Label Prédit")
    axs[1].legend()

    plt.xticks(rotation=45)
    plt.tight_layout()  # Optimisation de l'espacement des sous-graphes
    plt.show()

