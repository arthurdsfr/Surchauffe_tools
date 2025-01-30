import numpy as np
import matplotlib.pyplot as plt
import data.calculated_data.rsi as rs
import data.calculated_data.moving_average as ma
import data.calculated_data.variation_price as vp

def plot_indicators(df, coin_prices_365j):
    dates = np.arange(len(df))  # Création d'un axe temporel fictif

    fig, axs = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

    # Prix et Moyennes Mobiles
    axs[0].plot(dates, df['Prix (USD)'], label="Price", color='black')
    axs[0].plot(dates, ma.sma_50(coin_prices_365j), label="SMA50", linestyle="dashed", color='blue')
    axs[0].plot(dates, ma.sma_200(coin_prices_365j), label="SMA200", linestyle="dashed", color='red')
    axs[0].set_title("Prix et Moyennes Mobiles")
    axs[0].legend()

    # RSI
    axs[1].plot(dates, rs.rsi(coin_prices_365j), label="RSI", color='purple')
    axs[1].axhline(y=70, color='r', linestyle='dashed', label="Surachat (70)")
    axs[1].axhline(y=30, color='g', linestyle='dashed', label="Survente (30)")
    axs[1].set_title("RSI")
    axs[1].legend()

    # Variation du prix
    axs[2].plot(dates, vp.price_variation_1d(coin_prices_365j), label="VP_1d", color='orange')
    axs[2].plot(dates, vp.price_variation_7d(coin_prices_365j), label="VP_7d", color='blue')
    axs[2].plot(dates, vp.price_variation_30d(coin_prices_365j), label="VP_30d", color='red')
    axs[2].set_title("Variation du Prix")
    axs[2].legend()

    plt.xlabel("Jours")
    plt.tight_layout()
    plt.show()

def plot_results(df, predictions):
    dates = np.arange(len(df))  # Création d'un axe temporel fictif
    plt.figure(figsize=(12, 5))
    plt.plot(dates, predictions, label="Prédictions", marker='o', color='green')
    plt.title("Prédictions du Modèle")
    plt.xlabel("Dates")
    plt.ylabel("Label Prédit")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()