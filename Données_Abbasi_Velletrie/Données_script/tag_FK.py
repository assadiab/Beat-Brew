from faker import Faker
import random

fake = Faker()

# Plage d'ID pour les tags
plage_id_tag = list(range(1, 31))  # Adaptez cette plage en fonction du nombre de tags que vous avez

# Plages d'ID pour les autres tables
plage_id_lieu = list(range(1, 11))
plage_id_concert = list(range(1, 61))
plage_id_artistes = list(range(1, 31))  # Adaptez cette plage en fonction du nombre d'artistes que vous avez
plage_id_playlist = list(range(1, 31))  # Adaptez cette plage en fonction du nombre de playlists que vous avez
plage_id_avis = list(range(1, 71))  # Adaptez cette plage en fonction du nombre d'avis que vous avez

# Nombre de lignes à générer
nombre_lignes = 30  # Adaptez ce nombre en fonction de vos besoins

# Générer les données pour Tag_Lieu
with open("tag_lieu.sql", "w") as fichier:
    fichier.write("INSERT INTO Tag_Lieu (Tag_Id, Lieu_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        tag_id = random.choice(plage_id_tag)
        lieu_id = random.choice(plage_id_lieu)
        ligne_sql = f"({tag_id}, {lieu_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

# Générer les données pour Tag_Concert
with open("tag_concert.sql", "w") as fichier:
    fichier.write("INSERT INTO Tag_Concert (Tag_Id, Concert_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        tag_id = random.choice(plage_id_tag)
        concert_id = random.choice(plage_id_concert)
        ligne_sql = f"({tag_id}, {concert_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

# Générer les données pour Tag_Artistes
with open("tag_artistes.sql", "w") as fichier:
    fichier.write("INSERT INTO Tag_Artistes (Tag_Id, Artistes_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        tag_id = random.choice(plage_id_tag)
        artistes_id = random.choice(plage_id_artistes)
        ligne_sql = f"({tag_id}, {artistes_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

# Générer les données pour Tag_Playlist
with open("tag_playlist.sql", "w") as fichier:
    fichier.write("INSERT INTO Tag_Playlist (Tag_Id, Playlist_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        tag_id = random.choice(plage_id_tag)
        playlist_id = random.choice(plage_id_playlist)
        ligne_sql = f"({tag_id}, {playlist_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

# Générer les données pour Tag_Avis
with open("tag_avis.sql", "w") as fichier:
    fichier.write("INSERT INTO Tag_Avis (Tag_Id, Avis_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        tag_id = random.choice(plage_id_tag)
        avis_id = random.choice(plage_id_avis)
        ligne_sql = f"({tag_id}, {avis_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

print("Les données fictives pour les tables Tag_* ont été écrites.")
