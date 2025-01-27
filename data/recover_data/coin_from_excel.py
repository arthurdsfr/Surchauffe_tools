from sqlalchemy import create_engine
import pandas as pd
import pymysql

def fetch_eth_data_from_excel():

    engine = create_engine('mysql+pymysql://root:azerty@localhost/crypto_data')

    try:
        # Charger les données
        query = '''
        SELECT 
            `Prix (USD)`,
            `MarketCap (USD)`,
            `Volume (USD)`
        FROM solana_data
        '''

        # Lire les données dans un DataFrame
        Table = pd.read_sql(query, engine)

        # Extraire chaque colonne en liste
        eth_prices_365j = Table['Prix (USD)'].tolist()
        marketcap_365j = Table['MarketCap (USD)'].tolist()
        volume_24h_365j = Table['Volume (USD)'].tolist()

        # Retourner les listes
        return eth_prices_365j, marketcap_365j, volume_24h_365j

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return [], [], []

    finally:
        engine.dispose()


def fetch_30d_from_excel():

    engine = create_engine('mysql+pymysql://root:azerty@localhost/crypto_data')

    try:
        # Charger les données
        query = '''
        SELECT 
            `Prix (USD)`,
            `MarketCap (USD)`,
            `Volume (USD)`,
            ORDER BY `Date` DESC LIMIT 30
        FROM solana_data
        '''
        # Lire les données dans un DataFrame
        df = pd.read_sql(query, engine)

        # Inverser l'ordre des lignes pour avoir les données du plus ancien au plus récent
        df = df.iloc[::-1]

        # Retourner le DataFrame
        return df

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return pd.DataFrame()

    finally:
        engine.dispose()