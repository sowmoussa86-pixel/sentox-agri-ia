import sqlite3

connexion = sqlite3.connect("sentox.db")
curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    culture TEXT,
    pesticide TEXT,
    toxicite TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connexion.commit()

def sauvegarder_analyse(culture, pesticide, toxicite):
    curseur.execute("""
    INSERT INTO analyses (culture, pesticide, toxicite)
    VALUES (?, ?, ?)
    """, (culture, pesticide, toxicite))

    connexion.commit()

def lire_historique():
    curseur.execute("""
    SELECT * FROM analyses
    ORDER BY date DESC
    """)

    return curseur.fetchall()