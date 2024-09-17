# Bienvenue dans Python Pizza Deliveries
print("Bienvenue dans Python Pizza Deliveries!")

# Demander la taille de la pizza
taille = input("Quelle taille de pizza voulez-vous? (P/M/G) : ").upper()

# Demander si l'utilisateur veut du pepperoni
add_pepperoni = input("Voulez-vous du pepperoni? (Y/N) : ").upper()

# Demander si l'utilisateur veut du fromage supplémentaire
extra_cheese = input("Voulez-vous du fromage supplémentaire? (Y/N) : ").upper()

# Initialiser le prix de base de la pizza
prix = 0

# Déterminer le prix en fonction de la taille
if taille == "P":
    prix = 15
elif taille == "M":
    prix = 20
elif taille == "G":
    prix = 25
else:
    print("Taille de pizza invalide.")

# Ajouter le coût du pepperoni
if add_pepperoni == "Y":
    if taille == "P":
        prix += 2
    else:
        prix += 3

# Ajouter le coût du fromage
if extra_cheese == "Y":
    prix += 1

# Afficher la facture finale
print(f"Votre facture finale est de : {prix} $")