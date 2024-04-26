from faker import Faker
import random

fake = Faker()

# Nombre de concerts à générer
nombre_concerts = 60

# Plage d'ID_Lieu de 1 à 10
plage_id_lieu = list(range(1, 11))

# Nom du fichier SQL pour Concert
fichier_concert = "donnees_concert_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_concert, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Concert (Concert_Id, Nom, Date, Organisateurs, \"Line-up\", Nombre_places, Cause_soutien, Espace_exterieur, Enfants_permis, Prix, Nb_volontaires, ID_Lieu) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_concerts + 1):
        concert_id = i
        nom_concert = fake.company().replace("'", "''")
        date_concert = fake.date_between(start_date='-30d', end_date='+30d').strftime('%Y-%m-%d')
        organisateurs = fake.name().replace("'", "''")
        line_up = ', '.join([fake.sentence() for _ in range(3)])  # Utilisation de sentence() pour générer des noms d'artistes fictifs
        nombre_places = fake.random_int(min=50, max=500)
        cause_soutien = fake.boolean()
        espace_exterieur = fake.boolean()
        enfants_permis = fake.boolean()
        prix = fake.random.uniform(1000, 100000)
        nb_volontaires = fake.random_int(min=1, max=20)
        id_lieu = random.choice(plage_id_lieu)

        ligne_sql = f"({concert_id}, '{nom_concert}', '{date_concert}', '{organisateurs}', '{line_up}', {nombre_places}, {cause_soutien}, {espace_exterieur}, {enfants_permis}, {prix:.2f}, {nb_volontaires}, {id_lieu})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_concerts:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Concert ont été écrites dans {fichier_concert}")
