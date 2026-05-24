from pesticides import base_pesticides
from cultures import pesticides_db

print("\n===================================")
print("     SENTOX AGRI - IA")
print("===================================\n")

# =========================
# ENTRÉE UTILISATEUR
# =========================

culture = input("Entrer culture : ").lower().strip()

# =========================
# VÉRIFICATION CULTURE
# =========================

if culture in pesticides_db:

    data = pesticides_db[culture]

    print("\nPESTICIDES DISPONIBLES\n")

    for pesticide in data:

        nom = pesticide["nom"]

        print("================================")
        print("Nom :", nom)
        print("Dose recommandée :", pesticide["dose"], "L/ha")
        print("Risque :", pesticide["risque"])
        print("Efficacité :", pesticide["efficacite"], "/10")
        print("Autorisé :", pesticide["autorise"])

        # =========================
        # DONNÉES TOXICOLOGIQUES
        # =========================

        if nom in base_pesticides:

            info = base_pesticides[nom]

            print("\n----- DONNÉES TOXICOLOGIQUES -----")

            print("Toxicité :", info["toxicite"])

            print("DL50 :", info["DL50"])

            print("Risques :", info["risques"])

            print("Cancérogène :", info["cancerogene"])

            print("Écotoxique :", info["ecotoxique"])

            print("Danger abeilles :", info["abeilles"])

            print("Danger poissons :", info["poissons"])

        else:

            print("\nAucune donnée toxicologique trouvée")

        # =========================
        # SCORE RISQUE
        # =========================

        risque = pesticide["risque"]

        if risque == 1:
            score = "SAFE"

        elif risque == 2:
            score = "ATTENTION"

        else:
            score = "DANGER"

        print("\nSCORE SENTOX :", score)

        print("================================\n")

else:

    print("\n❌ Culture non reconnue")

    print("\nCultures disponibles :\n")

    for c in pesticides_db.keys():
        print("-", c)