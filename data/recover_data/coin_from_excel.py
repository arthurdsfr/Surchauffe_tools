import pandas as pd


def fetch_data_from_excel():
    try:
        # Définir le chemin du fichier Excel
        file_path = "C:\\Users\\arthu\\IdeaProjects\\Surchauffe_Tools\\data\\recover_data\\solana_data.xlsx"  # À modifier avec le bon chemin

        # Lire les données depuis l'Excel
        df = pd.read_excel(file_path, sheet_name=0)

        # Vérifier si les colonnes existent
        required_columns = ['Prix (USD)', 'MarketCap (USD)', 'Volume (USD)']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"La colonne '{col}' est absente du fichier Excel.")

        # Extraire chaque colonne en liste
        eth_prices_365j = df['Prix (USD)'].tolist()
        marketcap_365j = df['MarketCap (USD)'].tolist()
        volume_24h_365j = df['Volume (USD)'].tolist()

        # Retourner les listes
        return df, eth_prices_365j, marketcap_365j, volume_24h_365j

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return [], [], []


def fetch_60d_from_excel():
    try:
        # Définir le chemin du fichier Excel
        file_path = "C:\\Users\\arthu\\IdeaProjects\\Surchauffe_Tools\\data\\recover_data\\solana_data.xlsx"  # À modifier avec le bon chemin

        # Lire les données depuis l'Excel
        df = pd.read_excel(file_path, sheet_name=0)

        # Vérifier si les colonnes existent
        required_columns = ['Prix (USD)', 'MarketCap (USD)', 'Volume (USD)']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"La colonne '{col}' est absente du fichier Excel.")

        df = df.tail(60)
        # Extraire chaque colonne en liste
        eth_prices_365j = df['Prix (USD)'].tolist()
        marketcap_365j = df['MarketCap (USD)'].tolist()
        volume_24h_365j = df['Volume (USD)'].tolist()

        # Retourner les listes
        return df, eth_prices_365j, marketcap_365j, volume_24h_365j

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return [], [], []

