import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_course(topic: str, level: str, time: str) -> str:
    prompt = f"""
Tu es un expert en pédagogie écologique.

Crée un parcours d’apprentissage structuré et clair.

Sujet : {topic}
Niveau : {level}
Temps disponible : {time}

Le parcours doit contenir :
1. Une introduction
2. Des modules numérotés
3. Des objectifs pédagogiques
4. Un mini quiz de fin
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
