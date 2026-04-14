


import pandas as pd
import time
import sys
from loguru import logger
import psycopg2
from config import DB_CONFIG, MAX_RETRIES, DELAY, TABLE_NAME

def extracting_data_database(max_retries: int = MAX_RETRIES, delay: int = DELAY):
    """Extraction des données depuis PostgreSQL avec pg8000"""
    logger.info("Début de l'extraction des données depuis PostgreSQL")

    for retry in range(max_retries):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            # Forcer l'encodage après connexion
            #conn.set_client_encoding('WIN1252')
            
            df_brute = pd.read_sql(f"SELECT * FROM {TABLE_NAME};", conn)
            print("✅ Connexion réussie !")
            print(df_brute)
            conn.close()
            
            logger.success(f"Extraction réussie : {len(df_brute)} lignes depuis {TABLE_NAME}")
            return df_brute
            
        except Exception as e:
            logger.error(f"Erreur lors de l'extraction : {e}")
            if retry < max_retries - 1:
                logger.info(f"Tentative {retry+1}/{max_retries} échouée. Nouvelle tentative dans {delay}s")
                time.sleep(delay)
                delay *= 2
            else:
                logger.critical(f"Échec total après {max_retries} tentatives")
                sys.exit("Arrêt du programme : impossible de charger la source de données")