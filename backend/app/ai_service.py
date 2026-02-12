import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_course(topic, level, time):
    prompt = f"""
    Crée un parcours d'apprentissage écologique.
    Sujet : {topic}
    Niveau : {level}
    Temps disponible : {time}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
