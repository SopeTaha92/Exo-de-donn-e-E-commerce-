


import pandas as pd 
from loguru import logger


def cleanning_brute_data(df_brute : pd.DataFrame, clean_data : str):
    """La fonction qui se charge du néttoyage des données brutes"""

    logger.info('Début du néttoyage des données brutes')
    df = df_brute.copy()
    df = df.drop_duplicates() 

    column_text = ['customer_name', 'shipping_city', 'status', 'product_name', 'category']
    df[column_text] = df[column_text].apply(lambda x : x.str.strip().str.title()).fillna('Inconnu')

    df['customer_email'] = df['customer_email'].apply(lambda x : x.lower() if pd.notna(x) and '@' in x else None).fillna('email_manquant@domain.com')
    df['quantity'] = df['quantity'].astype(int)

    df['unit_price'] = (
        df['unit_price']
        .str.replace('€', '', regex=False)
        .str.replace(' ', '', regex=False)
        .replace('', 0, regex=False)
        .astype(float)
        .round(2)
    )

    df['discount'] = (
        df['discount']
        .str.replace('%', '', regex=False)
        .str.replace(' ', '', regex=False)
        .astype(int) / 100
    ) 

    df['order_date'] = pd.to_datetime(
        df['order_date'],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    ).dt.date



    df.to_csv(clean_data, index=False)
    logger.info('Néttoyage des données brutes reussi avec succée')
    return df

