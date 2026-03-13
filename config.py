

from datetime import datetime
from pathlib import Path


BRUTE_DATA_DIR = Path('data/raw')
BRUTE_DATA_FILE = BRUTE_DATA_DIR / "donnée_vente_e-commerce_brute.csv"

BRUTE_DATA_CLEAN_DIR = Path('data/processed')
BRUTE_DATA_CLEAN_DIR.mkdir(parents=True, exist_ok=True)
BRUTE_DATA_CLEAN_FILE = BRUTE_DATA_CLEAN_DIR / f"clean_data_vente_e-commerce_brute.csv"

TODAY = datetime.now().strftime('%d-%m-%Y_%H-%M')


BASE_DIR_LOGS = Path('logs')
BASE_DIR_LOGS.mkdir(parents=True, exist_ok=True)
LOG_FILE = BASE_DIR_LOGS / f"log_vente_e-commerce{TODAY}.log"


BASE_DIR_EXCEL = Path('output')
BASE_DIR_EXCEL.mkdir(parents=True, exist_ok=True)
EXCEL_FILE = BASE_DIR_EXCEL / f"donnée_vente_E-commerce_{TODAY}.xlsx"


MAX_RETRIES = 3
DELAY = 1

"""MIN_ORANGE = 0
MAX_ORANGE = 100
GREEN_VALUE = 100"""


# Dans config.py, ajoute un dictionnaire ou une section dédiée
# Paramètres de mise en forme Excel
EXCEL_FORMATTING = {
    'Montant_remise': {
        'min_orange': 0,
        'max_orange': 100,
        'green_value': 100,
        'red_value': 0  # Peut-être utile ?
    }
}

# Dans config.py
COULEURS_EXCEL = {
    'vert': '#C6EFCE',
    'rouge': '#FFC7CE',
    'orange': '#FFEB9C',
    'hearder': '#5BDA42'
}