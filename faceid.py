import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Titre de notre application
st.title("Détection de Visages avec OpenCV")

# Nous permettons à l'utilisateur de télécharger une image
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Nous lisons l'image téléchargée
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Nous convertissons l'image en niveaux de gris
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Nous chargeons le classificateur en cascade pour la détection de visage
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Nous détectons les visages
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Nous dessinons des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(image_np, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Nous affichons l'image avec les visages détectés
    st.image(image_np, caption='Image avec détection de visages', use_column_width=True)
