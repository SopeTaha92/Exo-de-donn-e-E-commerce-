



import pandas as pd
from loguru import logger




def analysis_by_status(df : pd.DataFrame):
    """La fonction qui se charge des analyses par catégorie"""
    logger.info("Début de l'analyse par statut")

    df_statut = (
        df.groupby('status', as_index=False)
        .agg(
            {
            'quantity' : 'sum',
            'total_price' : 'sum',
            'Montant_remise' : 'sum',
            'Ca_Net' : 'sum'
            }
        )
        .round(2)
        .sort_values(by='Ca_Net', ascending=False)
        
    )

    logger.info("Analyse par statut réussi avec succée")
    return df_statut


