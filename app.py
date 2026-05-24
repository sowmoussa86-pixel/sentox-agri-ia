from cultures import pesticides_db
from pesticides import base_pesticides

print("===================================")
print("   SENTOX AGRI - VERSION IA")
print("===================================")

surface = float(input("Entrer surface (ha) : "))

culture = input("Entrer culture : ").strip().lower()

# Vérification culture
if culture not in pesticides_db:
    print("\n❌ Culture non reconnue")
    print("\nCultures disponibles :")

    for c in pesticides_db.keys():
        print("-", c)

    exit()

# Récupération pesticides
liste_pesticides = pesticides_db[culture]

print("\n===================================")
print(" PESTICIDES DISPONIBLES ")
print("===================================")

for i, p in enumerate(liste_pesticides):

    nom = p["nom"]

    print(
        f"{i+1}. {nom} | "
        f"Risque={p['risque']} | "
        f"Efficacité={p['efficacite']}"
    )

print("===================================")

choix = int(input("Choisir pesticide : ")) - 1

if choix < 0 or choix >= len(liste_pesticides):
    print("❌ Choix invalide")
    exit()

selection = liste_pesticides[choix]

nom_pesticide = selection["nom"]

# Vérification pesticide
if nom_pesticide not in base_pesticides:
    print("❌ Pesticide absent de la base")
    exit()

data = base_pesticides[nom_pesticide]

# Calcul dose totale
dose_ha = selection["dose"]
dose_totale = dose_ha * surface

# Score SENTOX
score = (
    selection["efficacite"] * 2
    - selection["risque"]
)

# Interprétation
if score >= 15:
    niveau = "SAFE"

elif score >= 10:
    niveau = "MODÉRÉ"

else:
    niveau = "DANGEREUX"

# Affichage
print("\n===================================")
print(" RESULTATS IA SENTOX ")
print("===================================")

print(f"\nCulture : {culture}")
print(f"Pesticide : {nom_pesticide}")

print(f"\nSurface : {surface} ha")

print(f"\nDose recommandée : {dose_ha} L/ha")
print(f"Dose totale : {dose_totale} L")

print("\n----- TOXICOLOGIE -----")

print(f"DL50 : {data['DL50']}")
print(f"Toxicité : {data['toxicite']}")
print(f"Risques : {data['risques']}")

print("\n----- ECOTOXICOLOGIE -----")

print(f"Ecotoxique : {data['ecotoxique']}")
print(f"Abeilles : {data['abeilles']}")
print(f"Poissons : {data['poissons']}")

print("\n----- IA SENTOX -----")

print(f"Efficacité : {selection['efficacite']}/10")
print(f"Risque : {selection['risque']}/3")

print(f"\nSCORE SENTOX : {score}")
print(f"NIVEAU : {niveau}")

print("\n===================================")
print(" ANALYSE TERMINEE ")
print("===================================")