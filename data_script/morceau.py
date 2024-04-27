from faker import Faker
import random

fake = Faker()

# Nombre de morceaux à générer
nombre_morceaux = 100

# Genres musicaux possibles
genres_musicaux = ['Pop', 'Rock', 'Hip-hop', 'Rap', 'Jazz', 'Blues', 'Country', 'Electronic', 'Reggae', 'Classical']

# Nom du fichier SQL pour Morceau
fichier_morceau = "donnees_morceau_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_morceau, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Morceau (Morceau_Id, Titre, Nom_album, Genre) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_morceaux + 1):
        id_morceau = i  # Identifiant croissant de 1 à 100
        titre_morceau = fake.word()
        nom_album = fake.word()
        genre_musical = random.choice(genres_musicaux)

        ligne_sql = f"({id_morceau}, '{titre_morceau}', '{nom_album}', '{genre_musical}')"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_morceaux:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Morceau ont été écrites dans {fichier_morceau}")
