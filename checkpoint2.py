# Déclaration des structures de données
shopping_list = []  # Liste pour stocker les articles
shopping_dict = {}  # Dictionnaire pour stocker article: quantité
shopping_set = set()  # Ensemble pour les articles uniques

# Limite du nombre d'articles
MAX_ITEMS = 10

def afficher_menu():
    print("\n--- Menu de la liste de courses ---")
    print("1. Ajouter un article")
    print("2. Supprimer un article")
    print("3. Afficher la liste")
    print("4. Quitter")

def ajouter_article():
    if len(shopping_list) >= MAX_ITEMS:
        print("Vous avez atteint le nombre maximum d'articles.")
        return
    article = input("Entrez le nom de l'article à ajouter: ")
    quantite = int(input("Entrez la quantité: "))
    shopping_list.append(article)
    shopping_dict[article] = quantite
    shopping_set.add(article)
    print(f"Article '{article}' ajouté avec succès.")

def supprimer_article():
    article = input("Entrez le nom de l'article à supprimer: ")
    if article in shopping_list:
        shopping_list.remove(article)
        del shopping_dict[article]
        shopping_set.discard(article)
        print(f"Article '{article}' supprimé.")
    else:
        print(f"L'article '{article}' n'est pas dans la liste.")

def afficher_liste():
    if not shopping_list:
        print("Votre liste de courses est vide.")
    else:
        print("\nListe de courses :")
        for i, article in enumerate(shopping_list, start=1):
            quantite = shopping_dict.get(article, 1)
            print(f"{i}. {article} - Quantité : {quantite}")

# Boucle principale pour le menu
while True:
    afficher_menu()
    choix = input("Faites un choix (1-4): ")

    if choix == "1":
        ajouter_article()
    elif choix == "2":
        supprimer_article()
    elif choix == "3":
        afficher_liste()
    elif choix == "4":
        print("Au revoir!")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
