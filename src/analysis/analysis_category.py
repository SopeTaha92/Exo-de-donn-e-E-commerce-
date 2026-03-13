



import pandas as pd
from loguru import logger




def analysis_by_categories(df : pd.DataFrame):
    """La fonction qui se charge des analyses par catégorie"""
    logger.info("Début de l'analyse par catégorie")

    df_category = (
        df.groupby('category', as_index=False)
        .agg(
            {
            'unit_price' : 'first',
            'quantity' : 'sum',
            'total_price' : 'sum',
            'Montant_remise' : 'sum',
            'Ca_Net' : 'sum'
            }
        )
        .round(2)
        .sort_values(by='quantity', ascending=False)
        
    )

    logger.info("Analyse par catégorie réussi avec succée")
    return df_category


