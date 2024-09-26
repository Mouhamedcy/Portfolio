import numpy as np

# Créer le tableau des notes
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculer la moyenne, la médiane et l'écart type
mean = np.mean(grades)
median = np.median(grades)
std_dev = np.std(grades)

# Trouver le maximum et le minimum
max_grade = np.max(grades)
min_grade = np.min(grades)

# Trier les notes par ordre croissant
sorted_grades = np.sort(grades)

# Trouver l'index de la note la plus élevée
max_index = np.argmax(grades)

# Compter le nombre d'étudiants ayant obtenu un score supérieur à 90
num_above_90 = np.sum(grades > 90)

# Calculer le pourcentage d'étudiants ayant obtenu un score supérieur à 90
percentage_above_90 = np.mean(grades > 90) * 100

# Calculer le pourcentage d'étudiants ayant obtenu un score inférieur à 75
percentage_below_75 = np.mean(grades < 75) * 100

# Extraire toutes les notes supérieures à 90
high_performers = grades[grades > 90]

# Créer un nouveau tableau avec toutes les notes supérieures à 75
passing_grades = grades[grades > 75]

# Imprimer les résultats
print(f"Moyenne : {mean:.2f}")
print(f"Médiane : {median:.2f}")
print(f"Écart type : {std_dev:.2f}")
print(f"Note maximale : {max_grade}")
print(f"Note minimale : {min_grade}")
print(f"Notes triées : {sorted_grades}")
print(f"Index de la note maximale : {max_index}")
print(f"Nombre d'étudiants avec une note > 90 : {num_above_90}")
print(f"Pourcentage d'étudiants avec une note > 90 : {percentage_above_90:.2f}%")
print(f"Pourcentage d'étudiants avec une note < 75 : {percentage_below_75:.2f}%")
print(f"Notes supérieures à 90 : {high_performers}")
print(f"Notes supérieures à 75 : {passing_grades}")