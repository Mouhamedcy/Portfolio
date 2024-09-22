# Définition des fonctions mathématiques de base
def ajouter(a, b):
    return a + b


def soustraire(a, b):
    return a - b


def multiplier(a, b):
    return a * b


def diviser(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro."


# Dictionnaire des opérations
operations = {
    '+': ajouter,
    '-': soustraire,
    '*': multiplier,
    '/': diviser
}


def calculatrice():
    # Inviter l'utilisateur à entrer le premier nombre
    num1 = float(input("Entrez le premier nombre: "))

    while True:
        # Afficher les symboles d'opération disponibles
        print("Opérations disponibles :")
        for symbol in operations.keys():
            print(symbol)

        # Demander à l'utilisateur de sélectionner un symbole d'opération
        operation = input("Choisissez une opération (ou 'q' pour quitter) : ")

        if operation == 'q':
            print("Merci d'avoir utilisé la calculatrice.")
            break

        if operation not in operations:
            print("Opération invalide. Veuillez choisir une opération valide.")
            continue

        # Inviter l'utilisateur à entrer le deuxième nombre
        num2 = float(input("Entrez le deuxième nombre: "))

        # Récupérer la fonction correspondante et effectuer le calcul
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)

        # Afficher le résultat
        print(f"{num1} {operation} {num2} = {answer}")

        # Demander si l'utilisateur veut continuer avec le résultat
        should_continue = input("Voulez-vous continuer avec ce résultat comme premier nombre ? (oui/non) : ").lower()

        if should_continue == 'oui':
            num1 = answer  # Mettre à jour le premier nombre avec le résultat
        else:
            # Redémarrer le calcul
            calculatrice()
            break


# Démarrer la calculatrice
calculatrice()