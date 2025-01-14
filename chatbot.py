import streamlit as st
import openai

# Configure ton API Key OpenAI
openai.api_key = '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'

# Fonction pour obtenir la réponse du chatbot
def get_chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Assure-toi d'utiliser le modèle approprié
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

# Titre de l'application
st.title("Chatbot Interface")

# Zone de texte pour l'utilisateur
user_input = st.text_input("Posez votre question :")

# Bouton pour soumettre l'entrée
if st.button("Envoyer"):
    if user_input:
        response = get_chatbot_response(user_input)
        st.text_area("Réponse du chatbot :", value=response, height=200)
    else:
        st.warning("Veuillez entrer une question.")