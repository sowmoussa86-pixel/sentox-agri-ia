import google.generativeai as genai

# =========================
# CONFIGURATION GEMINI
# =========================

API_KEY = "VOTRE_CLE_API_GEMINI"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")


# =========================
# FONCTION GEMINI
# =========================

def demander_gemini(question):

    try:

        prompt = f"""
Tu es SENTOX AGRI AI.

Tu es expert en :
- toxicologie
- pesticides
- agriculture
- sécurité alimentaire
- FAO
- OMS

Réponds de manière professionnelle.

Question :
{question}
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Erreur Gemini : {e}"