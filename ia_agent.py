from gemini_api import demander_gemini


# =========================
# CORRECTIONS ORTHOGRAPHIQUES
# =========================

corrections = {

    "ginembre": "gingembre",
    "ginjembre": "gingembre",
    "gingenbre": "gingembre",

    "mais": "maïs",

    "poumedeterre": "pomme de terre",

    "niebe": "niébé",

    "harico": "haricot"

}


# =========================
# REPONSES LOCALES
# =========================

reponses_locales = {

    "glyphosate": """
GLYPHOSATE

- Herbicide systémique
- Toxicité : modérée

Risques :
- irritation peau
- pollution eau
- risque chronique

Dose :
2 à 4 L/ha

Conseils :
- porter EPI
- éviter surdosage
- respecter délai récolte
""",

    "paraquat": """
PARAQUAT

- Herbicide très toxique

Risques :
- intoxication aiguë
- lésions pulmonaires
- brûlures chimiques

Protection obligatoire :
- masque
- gants
- lunettes
""",

    "riz": """
Culture : Riz

Besoins en eau :
12000000 L/ha

Pesticides fréquents :
- paraquat
- glyphosate

Risque :
- toxicité modérée
""",

    "tomate": """
Culture : Tomate

Besoins en eau :
7000000 L/ha

Pesticides :
- mancozèbe
- cyperméthrine

Risque :
- toxicité élevée
"""
}


# =========================
# AGENT IA PRINCIPAL
# =========================

def agent_ia(question):

    try:

        question = question.lower()

        # Correction orthographique
        for faux, correct in corrections.items():

            question = question.replace(faux, correct)

        # Réponse locale
        for mot in reponses_locales.keys():

            if mot in question:

                return reponses_locales[mot]

        # IA Gemini
        response = demander_gemini(question)

        if response:

            return response

        return "Aucune réponse trouvée."

    except Exception as e:

        return f"Erreur agent IA : {e}"