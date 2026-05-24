from openai import OpenAI

API_KEY = "VOTRE_CLE_OPENAI"

client = OpenAI(api_key=API_KEY)

def demander_chatgpt(question):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Erreur OpenAI : {e}"