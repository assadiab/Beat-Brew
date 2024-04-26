from faker import Faker
import random

fake = Faker()

# Nombre de lignes à générer
nombre_lignes = 150

# Nom du fichier SQL pour Publication
fichier_publication = "donnees_publication_fictives.sql"

# Générer les données pour Publication
with open(fichier_publication, "w") as fichier:
    fichier.write("INSERT INTO Publication (Publication_ID, Date) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        publication_id = i
        date = fake.date_this_decade().strftime("%Y-%m-%d")
        ligne_sql = f"({publication_id}, '{date}')"
        if i < nombre_lignes:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Publication ont été écrites dans {fichier_publication}")
