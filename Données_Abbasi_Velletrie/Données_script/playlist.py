from faker import Faker
import random

fake = Faker()

# Nombre de playlists à générer
nombre_playlists = 30

# Plage d'ID_Utilisateur de 1 à 150
plage_id_utilisateur = list(range(1, 151))

# Nom du fichier SQL pour Playlist
fichier_playlist = "donnees_playlist_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_playlist, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Playlist (Playlist_Id, Nom, IsGroupe, Artistes_Id, Nb_morceau) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_playlists + 1):
        playlist_id = i  # Utilisation d'une séquence pour l'ID de la playlist
        nom_playlist = fake.word()
        is_groupe = fake.boolean()
        artistes_id = random.choice(plage_id_utilisateur)
        nb_morceau = random.randint(0, 20)

        ligne_sql = f"({playlist_id}, '{nom_playlist}', {is_groupe}, {artistes_id}, {nb_morceau})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_playlists:
            ligne_sql += ","

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Playlist ont été écrites dans {fichier_playlist}")


