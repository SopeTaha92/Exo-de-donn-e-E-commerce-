


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![psycopg2](https://img.shields.io/badge/psycopg2-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![pg8000](https://img.shields.io/badge/pg8000-1.31.5-0066B3?style=for-the-badge&logo=postgresql&logoColor=white)

# 📊 Pipeline d'Analyse E-commerce (10k - 1M+ lignes)

Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** robuste et modulaire. Il permet de transformer des données brutes de ventes en un rapport Excel décisionnel hautement visuel, avec une gestion centralisée des paramètres.

**Fonctionnalité clé** : Extraction des données depuis **PostgreSQL** (via `psycopg2` ou `pg8000`) avec mécanisme de retry, nettoyage avancé, enrichissement des données et génération automatisée de rapports Excel professionnels.

---

## 🌟 Points Forts du Projet

| Fonctionnalité | Description |
|----------------|-------------|
| **Double connectivité PostgreSQL** | Support de `psycopg2` (standard industriel) et `pg8000` (solution de contournement pour les problèmes d'encodage) |
| **Configuration Centralisée** | Gestion de tous les chemins (data, logs, output), constantes métiers **et paramètres de connexion DB** via `config.py` |
| **Robustesse (Retry Logic)** | Système d'extraction capable de gérer les indisponibilités (fichiers ou base de données) avec tentatives multiples et délai exponentiel |
| **Architecture Modulaire** | Séparation claire : extraction → nettoyage → calculs → analyses → reporting |
| **Gestion d'encodage avancée** | Traitement des caractères problématiques (`€`, `%`, accents) avec `pandas` et conversion explicite |
| **Visualisation Avancée** | Tableaux de bord Excel automatisés avec axes secondaires et formatage conditionnel |

---

## 🛠️ Architecture du Code

├── config.py              # ⚙️ Centre de contrôle (Chemins, Formats, Seuils, DB_CONFIG)
├── main.py                # 🚀 Point d'entrée du pipeline
├── src/
│   ├── extract.py         # 📥 Extraction depuis PostgreSQL (psycopg2/pg8000 + retry)
│   ├── clean.py           # 🧹 Nettoyage et typage (Pandas + gestion des caractères mal encodés)
│   ├── features.py        # 📈 Calcul d'indicateurs (Marge, Profit, Montant remisé)
│   ├── analysis/          # 🔍 Analyses spécifiques (Category, City, Status)
│   ├── logger.py          # 📝 Gestionnaire de logs (Loguru)
│   └── repport_excel.py   # 📊 Moteur de rendu XlsxWriter
├── data/                  # 💾 Dossier des sources (CSV - optionnel)
├── logs/                  # 📜 Historique d'exécution
└── output/                # 📂 Rapports générés


---

## ⚙️ Configuration Centralisée (`config.py`)

Le fichier `config.py` centralise tous les paramètres modifiables :

```python
# Chemins
BRUTE_DATA_DIR = Path('data/raw')
BRUTE_DATA_FILE = BRUTE_DATA_DIR / "donnée_vente_e-commerce_brute.csv"

# PostgreSQL
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'ecommerce_db',
    'user': 'sope',
    'password': 'azerty12'
}
TABLE_NAME = 'ventes_auto'

# Paramètres de retry
MAX_RETRIES = 3
DELAY = 1

# Formatage Excel
EXCEL_FORMATTING = { 
    'Montant_remise': {
        'min_orange': 0,
        'max_orange': 100,
        'green_value': 100
    }
 }

📊 Reporting Automatisé
Le rapport Excel généré contient 5 onglets stratégiques :

Onglet	Contenu
Données Brutes	Données extraites de PostgreSQL (avant nettoyage)
Données Nettoyées au Complet	Données après typage, suppression des doublons, correction des encodages
Données Par Catégories	Performance produit avec courbes de tendances (CA, quantités)
Données Par City	Répartition géographique des ventes (graphique circulaire + tableau)
Données Par Status	Monitoring du flux logistique (CA Net vs Remises par statut)
🐛 Difficultés rencontrées et solutions
1. Problème d'encodage avec psycopg2
Symptôme : UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9

Cause : Le caractère € présent dans la colonne unit_price était mal interprété par psycopg2 sur Windows (locale française).

Solutions testées :

Forcer client_encoding='WIN1252' dans la connexion

Nettoyer après extraction avec .str.encode('latin1').str.decode('utf8')

Solution retenue : Double approche

Nettoyage dans clean.py : remplacement de 'â\x82¬' par une chaîne vide

Fallback avec pg8000 (bibliothèque pure Python) en cas de problème persistant

2. Gestion des caractères mal encodés dans pandas
Symptôme : ValueError: could not convert string to float: '899.99â\x82¬'

Solution dans clean.py :
df['unit_price'] = (df['unit_price']
    .astype(str)
    .str.replace('â\x82¬', '', regex=False)
    .str.replace(',', '.')
    .str.strip()
)
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

3. Transition CSV → PostgreSQL
Défi : Remplacer la lecture CSV par une extraction SQL sans casser le pipeline existant.

Solution :

Ajout d'une configuration DB_CONFIG et TABLE_NAME dans config.py

Modification de extract.py pour supporter les deux sources (CSV ou DB) via un paramètre

Conservation du clean.py intact (le nettoyage reste valable)

4. Avertissement pandas avec pg8000
Symptôme : UserWarning: pandas only supports SQLAlchemy connectable...

Solution : Avertissement sans conséquence. Peut être ignoré ou filtré avec warnings.filterwarnings(). Utilisation de psycopg2 pour l'éviter.

🔧 Dépendances principales

| Bibliothèque      | Version | Utilité |
|--------------     |---------|---------|
| `psycopg2-binary` | 2.9.11  | Connexion PostgreSQL standard |
| `pg8000`          | 1.31.5  | Alternative pure Python (fallback encodage) |
| `pandas`          | 3.0.1   | Manipulation et nettoyage des données |
| `loguru`          | 0.7.3   | Logging structuré |
| `xlsxwriter`      | 3.2.9   | Génération de rapports Excel avancés |

🚀 Installation & Lancement

# 1. Cloner le dépôt
git clone https://github.com/SopeTaha92/Projet_vente_e-commerce.git
cd Projet_vente_e-commerce

# 2. Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer PostgreSQL (si utilisation base de données)
#    - Créer une base 'ecommerce_db'
#    - Importer les données dans une table 'ventes_auto'
#    - Adapter DB_CONFIG dans config.py

# 5. Exécuter le pipeline
python main.py

📈 Évolutions futures
Ajout d'index sur la table PostgreSQL pour accélérer les requêtes

Déplacement des calculs pandas vers des requêtes SQL (vues matérialisées)

Orchestration avec Apache Airflow ou Prefect

Ajout de tests unitaires (pytest)

Dashboard interactif avec Streamlit ou Power BI

📝 License
Ce projet est open source et disponible sous la licence MIT.


---

## ✅ Ce que j'ai ajouté / amélioré

| Section | Ajouts |
|---------|--------|
| **Badges** | Ajout des badges PostgreSQL et psycopg2 |
| **Points Forts** | Double connectivité, gestion d'encodage |
| **Architecture** | Précision sur le rôle de chaque fichier |
| **Configuration** | Exemple concret de `DB_CONFIG` |
| **Difficultés rencontrées** | 4 problèmes détaillés avec symptômes, causes et solutions |
| **Dépendances** | Tableau expliquant l'utilité de chaque bibliothèque |
| **Installation** | Étapes détaillées pour PostgreSQL |
| **Évolutions futures** | Liste des prochaines améliorations possibles |

---

**Tu peux copier-coller ce README dans ton dépôt GitHub. Il est prêt à être utilisé.**

## 👨‍💻 Auteur

**Mahmoud At-Tidiane** - Passionné par l'ingénierie des données, l'analyse décisionnelle et l'intégration PostgreSQL.

- GitHub : [@SopeTaha92](https://github.com/SopeTaha92)
- Projet : [Projet_vente_e-commerce](https://github.com/SopeTaha92/Projet_vente_e-commerce)
