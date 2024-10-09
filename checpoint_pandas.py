import pandas as pd

# Créer le DataFrame
data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
    'Experience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)

# Sélectionner les 3 premières lignes en utilisant iloc
premieres_trois_lignes = employee_df.iloc[:3]

# Sélectionner toutes les lignes où le département est "Marketing" en utilisant loc
employes_marketing = employee_df.loc[employee_df['Department'] == 'Marketing']

# Sélectionner les colonnes Age et Gender pour les 4 premières lignes en utilisant iloc
age_genre_quatre_premieres = employee_df.iloc[:4, [2, 3]]  # Colonnes 2 (Age) et 3 (Gender)

# Sélectionner les colonnes Salary et Experience pour toutes les lignes où le genre est "Male" en utilisant loc
salaire_experience_hommes = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]

# Afficher les résultats
print("Les 3 premières lignes :")
print(premieres_trois_lignes)
print("\nEmployés du département Marketing :")
print(employes_marketing)
print("\nÂge et genre pour les 4 premières lignes :")
print(age_genre_quatre_premieres)
print("\nSalaire et expérience pour les employés masculins :")
print(salaire_experience_hommes)