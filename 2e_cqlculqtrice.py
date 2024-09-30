import math


class Calculatrice:
    def __init__(self):
        # Dictionnaire pour stocker les opérations mathématiques
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        # Ajout des opérations avancées
        self.add_operation('**', self.exponentiation)
        self.add_operation('sqrt', self.square_root)
        self.add_operation('log', self.logarithm)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Erreur : Division par zéro.")
        return a / b

    def exponentiation(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Erreur : La racine carrée d'un nombre négatif n'est pas définie.")
        return math.sqrt(a)

    def logarithm(self, a):
        if a <= 0:
            raise ValueError("Erreur : Le logarithme d'un nombre non positif n'est pas défini.")
        return math.log(a)

    def add_operation(self, symbole, fonction):
        self.operations[symbole] = fonction

    def calculate(self, a, symbole, b=None):
        if symbole not in self.operations:
            raise ValueError(f"Erreur : L'opération '{symbole}' n'est pas valide.")
        if not (isinstance(a, (int, float)) and (b is None or isinstance(b, (int, float)))):
            raise TypeError("Erreur : Les entrées doivent être des nombres.")

        if symbole in ['+', '-', '*', '/']:
            return self.operations[symbole](a, b)
        elif symbole in ['sqrt', 'log']:
            return self.operations[symbole](a)
        else:
            return self.operations[symbole](a, b)


def main():
    calc = Calculatrice()
    while True:
        try:
            print("\nOpérations disponibles : +, -, *, /, ** (exponentiation), sqrt (racine carrée), log (logarithme)")
            operation = input("Entrez l'opération (ou 'q' pour quitter) : ")
            if operation == 'q':
                break
            if operation in ['sqrt', 'log']:
                a = float(input("Entrez un nombre : "))
                result = calc.calculate(a, operation)
            else:
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
                result = calc.calculate(a, operation, b)

            print(f"Résultat : {result}")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()