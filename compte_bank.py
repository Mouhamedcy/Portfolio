class Account:
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



if __name__ == "__main__":
    # Création d'une instance de la classe Account
    my_account = Account("123456789", "Alice", 100.0)

    # Dépôt et retrait d'argent
    my_account.deposit(50.0)   
    my_account.withdraw(30.0)  
    print(f"Solde actuel: {my_account.check_balance()} $") 

    # Création d'une autre instance pour tester
    another_account = Account("987654321", "Bob", 200.0)
    another_account.deposit(100.0)  
    another_account.withdraw(250.0)  
    print(f"Solde actuel: {another_account.check_balance()} $") 
