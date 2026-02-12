import os
from openai import OpenAI

def generate_course(topic: str, level: str, time: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    # 🔒 Vérification clé API
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY manquante")

    client = OpenAI(api_key=api_key)

    prompt = f"""
Tu es un expert en pédagogie écologique.

Crée un parcours d’apprentissage structuré.

Sujet : {topic}
Niveau : {level}
Temps disponible : {time}

Le parcours doit contenir :
- Une introduction
- Des modules clairs
- Des conseils pratiques
- Un mini quiz final
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700
        )

        return response.choices[0].message.content

    except Exception as e:
        # ⚠️ Log serveur Render
        print("ERREUR OPENAI:", str(e))

        # ⚠️ Message utilisateur
        return (
            "⚠️ Impossible de générer le cours pour le moment.\n\n"
            "Vérifie la clé API OpenAI ou réessaie plus tard."
        )
