


import pandas as pd 
from loguru import logger
from typing import Dict


def repporting_excel(file : str, onglets : Dict[str , pd.DataFrame]):
    """La fonction qui se charge de la génération des fichiers Excel"""
    logger.info("Début de la génération du fichier Excel multi-onglets")
    with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
        workbook = writer.book

        for name, data in onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            worksheet = writer.sheets[name]
            for i, column in enumerate(data.columns):
                column_letter = data[column].astype(str).str.len().max()
                column_letter = max(column_letter, len(column)) + 3
                worksheet.set_column(i, i, column_letter)

