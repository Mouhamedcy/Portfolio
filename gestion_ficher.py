import numpy as np

# Ouvrir le fichier CSV
with open('Loan_prediction_dataset.csv', 'r') as file:
    # Charger les données en utilisant genfromtxt
    data = np.genfromtxt(file, delimiter=',', dtype=None, encoding='utf-8', names=True)

# Extraire les montants des prêts
loan_amounts = data['LoanAmount']

# Calculer la moyenne, la médiane et l'écart type
mean_loan_amount = np.mean(loan_amounts[~np.isnan(loan_amounts)])  # Ignorer les NaN
median_loan_amount = np.median(loan_amounts[~np.isnan(loan_amounts)])
std_loan_amount = np.std(loan_amounts[~np.isnan(loan_amounts)])

# Afficher les résultats
print(f"Moyenne des montants des prêts : {mean_loan_amount}")
print(f"Médiane des montants des prêts : {median_loan_amount}")
print(f"Écart type des montants des prêts : {std_loan_amount}")