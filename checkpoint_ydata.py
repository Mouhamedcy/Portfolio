import pandas as pd
from ydata_profiling import ProfileReport

# Charger l'ensemble de données dans un dataframe pandas
df = pd.read_csv('C:/Users/HP/Desktop/Python/python test-install/Tunisair_flights_dataset.csv')

# Partie 1 : Exploration des données avec Pandas

# Vue d'ensemble des données
print("Aperçu des données :")
print(df.head())
print("\nInformations sur le dataframe :")
print(df.info())

# Recherche des valeurs manquantes
missing_values = df.isnull().sum()
print("\nValeurs manquantes par colonne :")
print(missing_values[missing_values > 0])

# Statistiques récapitulatives
stats_summary = df.describe()
print("\nStatistiques récapitulatives :")
print(stats_summary)

# Partie 2 : Exploration des données avec ydata-Profiling

# Générer un rapport de profilage
profile = ProfileReport(df, title="Profiling Report for Tunisair Flights Dataset", explorative=True)

# Enregistrer le rapport sous forme de fichier HTML
profile.to_file("C:/Users/HP/Desktop/Python/python test-install/Tunisair_flights_profile_report.html")
