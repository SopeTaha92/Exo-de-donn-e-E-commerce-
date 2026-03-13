


import pandas as pd
from loguru import logger



def add_features(df : pd.DataFrame):
    """La fonction qui ajoutes des colonnes supplémentaire"""
    logger.info("Début de l'ajout des features")


    df['total_price'] = round((df['quantity'] * df['unit_price']), 2).astype(float)
    df['Montant_remise'] = round((df['total_price'] * df['discount']), 2).astype(float)
    df['Ca_Net'] = round((df['total_price'] - df['Montant_remise']), 2).astype(float)



    logger.info('Ajout des features réussi avec succée')
    return df