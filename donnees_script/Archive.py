from faker import Faker
import random

fake = Faker()

# Nombre d'archives à générer
nombre_archives = 25

# Plage d'ID_Concert 
plage_id_concert = list(range(1, 26))

# Plage d'Avis_Id 
plage_avis_id = list(range(1, 26))

# Nom du fichier SQL pour Archive
fichier_archive = "donnees_archive_fictives.sql"


with open(fichier_archive, "w") as fichier:

    fichier.write("INSERT INTO Archive (Archive_Id, Concert_Id, Avis_Id, Date_archivage, Nb_participants, Avis_participants, Photo_path, Video_path) VALUES\n")

    for i in range(1, nombre_archives + 1):
        archive_id = i
        concert_id = random.choice(plage_id_concert)
        avis_id = random.choice(plage_avis_id)
        date_archivage = fake.date_between(start_date='-365d', end_date='-1d').strftime('%Y-%m-%d')
        nb_participants = fake.random_int(min=50, max=500)
        avis_participants = fake.text(max_nb_chars=200)
        photo_path = f"/chemin/vers/photos/{fake.file_name()}"
        video_path = f"/chemin/vers/videos/{fake.file_name()}"

        ligne_sql = f"({archive_id}, {concert_id}, {avis_id}, '{date_archivage}', {nb_participants}, '{avis_participants}', '{photo_path}', '{video_path}')"

        if i < nombre_archives:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Archive ont été écrites dans {fichier_archive}")
