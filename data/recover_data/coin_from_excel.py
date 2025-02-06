import pandas as pd


def fetch_data_from_excel():
    try:
        # Définir le chemin du fichier Excel
        file_path = "C:\\Users\\arthu\\PycharmProjects\\Surchauffe_Tools\\data\\recover_data\\BTCUSDT.xlsx"  # À modifier avec le bon chemin

        # Lire les données depuis l'Excel
        df = pd.read_excel(file_path, sheet_name=0)

        # Vérifier si les colonnes existent
        required_columns = ['Close', 'Number of Trades', 'Volume']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"La colonne '{col}' est absente du fichier Excel.")

        # Extraire chaque colonne en liste
        coin_prices = df['Close'].tolist()
        number_trades = df['Number of Trades'].tolist()
        volume_24h = df['Volume'].tolist()

        # Retourner les listes
        return df, coin_prices, number_trades, volume_24h

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return [], [], []


def fetch_60d_from_excel():
    try:
        # Définir le chemin du fichier Excel
        file_path = "C:\\Users\\arthu\\PycharmProjects\\Surchauffe_Tools\\data\\recover_data\\BTCUSDT.xlsx"  # À modifier avec le bon chemin

        # Lire les données depuis l'Excel
        df = pd.read_excel(file_path, sheet_name=0)

        # Vérifier si les colonnes existent
        required_columns = ['Close', 'Number of Trades', 'Volume']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"La colonne '{col}' est absente du fichier Excel.")

        df = df.tail(60)
        # Extraire chaque colonne en liste
        coin_prices = df['Close'].tolist()
        number_trades = df['Number of Trades'].tolist()
        volume_24h = df['Volume'].tolist()

        # Retourner les listes
        return df, coin_prices, number_trades, volume_24h

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return [], [], []

