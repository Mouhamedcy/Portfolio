# Importation des bibliothèques nécessaires
import pandas as pd

# Chargement du jeu de données à partir du fichier CSV
df = pd.read_csv('C:/Users/HP/Downloads/STEG_BILLING_HISTORY.csv')

# Affichage des 10 premières lignes et stockage dans une variable appelée "client_0_bills"
client_0_bills = df.head(10)
print(client_0_bills)

# Vérification du type de données de la variable 'client_0_bills'
print(type(client_0_bills))

# Affichage des informations générales sur l'ensemble de données
df.info()

# Réponses aux questions basées sur l'inspection des informations générales :
# Combien de lignes et de colonnes avons-nous dans cet ensemble de données ?
n_rows, n_columns = df.shape
print(f"Nombre de lignes: {n_rows}, Nombre de colonnes: {n_columns}")

# Combien de fonctionnalités catégorielles sont présentes dans l'ensemble de données ?
categorical_features = df.select_dtypes(include=['object']).columns
print(f"Fonctionnalités catégorielles: {len(categorical_features)}")
print(categorical_features)

# Combien d'espace mémoire l'ensemble de données consomme-t-il ?
print(df.memory_usage(deep=True).sum())

# Inspection des valeurs manquantes
missing_values = df.isnull().sum()
print("Valeurs manquantes par colonne:")
print(missing_values)

# Stratégie de gestion des valeurs manquantes : Suppression des lignes avec des valeurs manquantes pour simplifier l'analyse.
# Justification : On choisit de supprimer les lignes car si les données manquantes représentent une faible proportion du dataset,
# cela peut ne pas affecter l'analyse.
df_clean = df.dropna()

# Analyse descriptive des fonctionnalités numériques
descriptive_stats = df_clean.describe()
print(descriptive_stats)

# Sélection des enregistrements de factures pour le client avec un identifiant = 'train_Client_0' méthode 1
client_0_records = df_clean[df_clean['client_id'] == 'train_Client_0']

# Sélection des enregistrements de factures pour le client avec un identifiant = 'train_Client_0' méthode 2
client_0_records_alt = df_clean.query("client_id == 'train_Client_0'")

# Transformation de la fonctionnalité 'counter_type' en variable numérique à l'aide d'un LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df_clean['counter_type_encoded'] = le.fit_transform(df_clean['counter_type'])

# Suppression de la fonctionnalité "counter_statue" du DataFrame
df_clean = df_clean.drop(columns=['counter_statue'])

# Affichage du DataFrame nettoyé
print(df_clean.head())
