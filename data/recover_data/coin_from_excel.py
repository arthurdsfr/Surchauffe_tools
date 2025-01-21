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
        FROM eth_data
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

