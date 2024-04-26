from faker import Faker
import random

fake = Faker()

# Nombre d'intérêts à générer
nombre_interets = 20

# Plage d'ID_Concert de 1 à 60
plage_id_concert = list(range(1, 61))

# Plage d'ID_Personne de 17 à 37
plage_id_personne = list(range(17, 38))

# Nom du fichier SQL pour Interet
fichier_interet = "donnees_interet_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_interet, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Interet (Concert_ID, Personne_ID) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_interets + 1):
        concert_id = random.choice(plage_id_concert)
        personne_id = random.choice(plage_id_personne)

        ligne_sql = f"({concert_id}, {personne_id})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_interets:
            ligne_sql += ","

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Interet ont été écrites dans {fichier_interet}")
