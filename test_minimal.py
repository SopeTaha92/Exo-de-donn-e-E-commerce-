





import pandas as pd
import psycopg2
import config

try:
    conn = psycopg2.connect(**config.DB_CONFIG)
    print("✅ psycopg2 fonctionne !")
    
    df = pd.read_sql("SELECT * FROM ventes_auto LIMIT 5;", conn)
    print("✅ Connexion réussie !")
    print(df)
    
    conn.close()
except Exception as e:
    print(f"❌ Erreur : {e}")




"""from config import DB_CONFIG, TABLE_NAME
import pg8000
import pandas as pd

print("Configuration :")
print(f"  Base : {DB_CONFIG['dbname']}")
print(f"  Table : {TABLE_NAME}")

try:
    conn = pg8000.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['dbname'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    
    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME} LIMIT 5;", conn)
    print(f"✅ Succès ! {len(df)} lignes")
    print(df.head())
    conn.close()
    
except Exception as e:
    print(f"❌ Erreur : {e}")
    850 MAMY
    7000 Père
"""


"""try:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='ecommerce_db',
        user='sope',
        password='azerty12'
    )
    print("✅ psycopg2 fonctionne !")
    conn.close()
except Exception as e:
    print(f"❌ Erreur : {e}")"""