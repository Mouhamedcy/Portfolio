"""class Account:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self.account_holder = account_holder

    def deposit(self, amount: float):
        """Ajoute le montant au solde du compte."""
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount} $ effectué. Nouveau solde: {self.balance} $")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount: float):
        """Soustrait le montant du solde du compte si le solde est suffisant."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Retrait de {amount} $ effectué. Nouveau solde: {self.balance} $")
            else:
                print("Fonds insuffisants pour ce retrait.")
        else:
            print("Le montant du retrait doit être positif.")

    def check_balance(self) -> float:
        """Renvoie le solde actuel du compte."""
        return self.balance


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de la classe Account
    my_account = Account("123456789", "Alice", 100.0)

    # Dépôt et retrait d'argent
    my_account.deposit(50.0)   # Dépôt de 50 $
    my_account.withdraw(30.0)  # Retrait de 30 $
    print(f"Solde actuel: {my_account.check_balance()} $")  # Vérification du solde

    # Création d'une autre instance pour tester
    another_account = Account("987654321", "Bob", 200.0)
    another_account.deposit(100.0)  # Dépôt de 100 $
    another_account.withdraw(250.0)  # Tentative de retrait de 250 $ (devrait échouer)
    print(f"Solde actuel: {another_account.check_balance()} $")  # Vérification du solde"""

import streamlit as st


class Account:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self.account_holder = account_holder

    def deposit(self, amount: float):
        """Ajoute le montant au solde du compte."""
        if amount > 0:
            self.balance += amount
            return f"Dépôt de {amount} $ effectué. Nouveau solde: {self.balance} $"
        else:
            return "Le montant du dépôt doit être positif."

    def withdraw(self, amount: float):
        """Soustrait le montant du solde du compte si le solde est suffisant."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Retrait de {amount} $ effectué. Nouveau solde: {self.balance} $"
            else:
                return "Fonds insuffisants pour ce retrait."
        else:
            return "Le montant du retrait doit être positif."

    def check_balance(self) -> float:
        """Renvoie le solde actuel du compte."""
        return self.balance


# Titre de l'application
st.title("Application de Gestion de Compte Bancaire")

# Formulaire pour créer un nouveau compte
account_number = st.text_input("Numéro de compte:")
account_holder = st.text_input("Titulaire du compte:")
initial_balance = st.number_input("Solde initial:", min_value=0.0, value=0.0, format="%.2f")

if st.button("Créer le compte"):
    my_account = Account(account_number, account_holder, initial_balance)
    st.success(f"Compte créé pour {my_account.account_holder} avec un solde de {my_account.check_balance()} $.")

# Interface pour les transactions
if 'account' in locals():
    st.write(f"Compte actuel: {my_account.account_holder} - Solde: {my_account.check_balance()} $")

    # Dépôt
    deposit_amount = st.number_input("Montant à déposer:", min_value=0.0, value=0.0, format="%.2f")
    if st.button("Déposer"):
        message = my_account.deposit(deposit_amount)
        st.info(message)

    # Retrait
    withdraw_amount = st.number_input("Montant à retirer:", min_value=0.0, value=0.0, format="%.2f")
    if st.button("Retirer"):
        message = my_account.withdraw(withdraw_amount)
        st.info(message)

    # Vérification du solde
    if st.button("Afficher le solde"):
        st.write(f"Solde actuel: {my_account.check_balance()} $")