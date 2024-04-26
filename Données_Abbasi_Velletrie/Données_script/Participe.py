from faker import Faker
import random

fake = Faker()

# Nombre de participations à générer
nombre_participations = 15

# Plage d'ID_Concert de 1 à 15
plage_id_concert = list(range(1, 15))

# Plage d'ID_Personne de 1 à 15
plage_id_personne = list(range(1, 15))

# Nom du fichier SQL pour Participe
fichier_participe = "donnees_participe_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_participe, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Participe (Concert_ID, Personne_ID) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_participations + 1):
        concert_id = random.choice(plage_id_concert)
        personne_id = random.choice(plage_id_personne)

        ligne_sql = f"({concert_id}, {personne_id})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_participations:
            ligne_sql += ","

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Participe ont été écrites dans {fichier_participe}")
