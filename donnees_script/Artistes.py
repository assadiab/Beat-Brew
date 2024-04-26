from faker import Faker
import random

fake = Faker()

# Nombre de groupes à générer
nombre_groupes = 100

# Liste des genres musicaux
genres_musicaux = ['KPop', 'Rock', 'Hip-hop', 'Rap', 'Jazz', 'Blues', 'Country', 'Electronic', 'Metal', 'Classical']

# Nom du fichier SQL pour Groupe
fichier_artistes = "artistes.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_artistes, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Artistes (Artistes_ID, Nom, Genre, Nb_Membres) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_groupes + 1):
        groupe_id = i
        nom_groupe = fake.company().replace("'", "''")
        genre_groupe = random.choice(genres_musicaux)
        nb_membres = random.randint(3, 10)

        ligne_sql = f"({groupe_id}, '{nom_groupe}', '{genre_groupe}', {nb_membres})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_groupes:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Groupe ont été écrites dans {fichier_artistes}")
