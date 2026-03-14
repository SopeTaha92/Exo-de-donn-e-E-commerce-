


📊 Pipeline d'Analyse E-commerce (10k - 1M+ lignes)

Ce projet implémente un pipeline ETL (Extract, Transform, Load) robuste et modulaire. Il permet de transformer des données brutes de ventes en un rapport Excel décisionnel hautement visuel, avec une gestion centralisée des paramètres.

🌟 Points Forts du Projet
Configuration Centralisée : Gestion de tous les chemins (data, logs, output) et constantes métiers via un fichier config.py.

Robustesse (Retry Logic) : Système d'extraction capable de gérer les indisponibilités fichiers avec tentatives multiples.

Architecture Modulaire : Séparation claire entre l'extraction, le nettoyage, l'analyse par thématiques et le reporting.

Visualisation Avancée : Tableaux de bord Excel automatisés avec axes secondaires et formatage conditionnel.

🛠️ Architecture du Code


├── config.py              # ⚙️ Centre de contrôle (Chemins, Formats, Seuils)
├── main.py                # 🚀 Point d'entrée du pipeline
├── src/
│   ├── extract.py         # 📥 Extraction avec logique de résilience
│   ├── clean.py           # 🧹 Nettoyage et typage (Pandas)
│   ├── features.py        # 📈 Calcul d'indicateurs (Marge, Profit, etc.)
│   ├── analysis/          # 🔍 Analyses spécifiques (Category, City, Status)
│   ├── logger.py          # 📝 Gestionnaire de logs (Loguru)
│   └── repport_excel.py   # 📊 Moteur de rendu XlsxWriter
├── data/                  # 💾 Dossier des sources (CSV)
├── logs/                  # 📜 Historique d'exécution
└── output/                # 📂 Rapports générés


⚙️ Centralisation avec config.py

Grâce au fichier config.py, la maintenance est simplifiée. Vous pouvez modifier en un seul endroit :

Les chemins des dossiers sources et destinations.

Les couleurs et seuils du formatage conditionnel (ex: Marge < 10% en rouge).

Les paramètres de la boucle de répétition (Max Retries).

📊 Reporting Automatisé
Le rapport généré contient 5 onglets stratégiques :

1 - Données Brutes & Nettoyées : Transparence totale sur la donnée.

2 - Par Catégories : Performance produit avec courbes de tendances.

3 - Par City : Répartition géographique des ventes (Pie Chart).

4 - Par Status : Monitoring du flux logistique (CA Net vs Remises).


🚀 Installation & Lancement

Bash

# 1. Cloner
git clone https://github.com/SopeTaha92/Projet_vente_e-commerce.git

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Exécuter
python main.py

Projet en constante évolution vers une intégration PostgreSQL

Développé par Mahmoud At-Tidiane - Passionné par l'ingénierie des données et l'analyse décisionnelle.