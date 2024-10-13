import pandas as pd
from ydata_profiling import ProfileReport

# Lire le fichier CSV dans un DataFrame Pandas
chemin_du_fichier = r"C:\Users\HP\Desktop\Python\python test-install\EDUCATION_ATTAINMENT.csv"
df = pd.read_csv(chemin_du_fichier)

# Afficher des informations générales sur le DataFrame
print(df.info())

# Étape 4: Exécuter une analyse descriptive sur le DataFrame
print(df.describe())

# Générer un rapport de profilage avec ydata-profiling
rapport = ProfileReport(df, title="Profil de l'enseignement", explorative=True)
rapport.to_file("rapport_education_attaintement.html")

# Afficher le rapport dans le navigateur (facultatif)
import webbrowser
webbrowser.open("rapport_education_attaintement.html")