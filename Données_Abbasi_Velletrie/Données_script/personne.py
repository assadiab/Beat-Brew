from faker import Faker
import random

fake = Faker()

# Nombre de lignes à générer
nombre_lignes = 60

# Nom du fichier SQL pour Personne
fichier_personne = "donnees_personne_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_personne, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Personne (Personne_ID, Age, Genre, Nationnalite) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_lignes + 1):  # Commencer à partir de 1 pour respecter les ID de 1 à 60
        personne_id = i
        utilisateur_id = personne_id  # Utiliser le même ID pour Personne et Utilisateur
        age = random.randint(18, 80)
        genre = random.choice(['M', 'F'])
        nationalite = fake.country()

        ligne_sql = f"({utilisateur_id}, {age}, '{genre}', '{nationalite}')"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_lignes:
            ligne_sql += ","

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Personne ont été écrites dans {fichier_personne}")
