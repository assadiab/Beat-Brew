from faker import Faker
import random

fake = Faker()

# Nombre d'annonces à générer
nombre_annonces = 25

# Plage d'ID_Utilisateur 
plage_id_utilisateur = list(range(1, 151))

# Plage d'ID_Concert 
plage_id_concert = list(range(1, 61))

# Nom du fichier SQL pour Annonce_Concert
fichier_annonce_concert = "donnees_annonce_concert_fictives.sql"

with open(fichier_annonce_concert, "w") as fichier:

    fichier.write("INSERT INTO Annonce_Concert (Annonce_Id, Utilisateur_Id, Concert_Id, Date_annonce) VALUES\n")

    for i in range(1, nombre_annonces + 1):
        annonce_id = i
        utilisateur_id = random.choice(plage_id_utilisateur)
        concert_id = random.choice(plage_id_concert)
        date_annonce = fake.date_between_dates(date_start=fake.date_between(start_date='-365d', end_date='today')).strftime('%Y-%m-%d')

        ligne_sql = f"({annonce_id}, {utilisateur_id}, {concert_id}, '{date_annonce}')"

        if i < nombre_annonces:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Annonce_Concert ont été écrites dans {fichier_annonce_concert}")

