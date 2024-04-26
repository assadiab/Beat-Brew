import random

# Nombre de lignes à générer
nombre_lignes = 150

# Plage d'ID de Playlist et Morceau
plage_id_playlist = list(range(1, 31))  # Supposons 30 playlists existent
plage_id_morceau = list(range(1, 101))   # Supposons 100 morceaux existent

# Nom du fichier SQL pour PlaylistMorceau
fichier_playlist_morceau = "donnees_playlist_morceau_fictives.sql"

# Ensemble pour suivre les combinaisons déjà générées
combinaisons_deja_generees = set()

# Ouvrir le fichier en mode écriture
with open(fichier_playlist_morceau, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO PlaylistMorceau (Playlist_Id, Morceau_Id) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_lignes + 1):
        # Générer une combinaison unique
        while True:
            id_playlist = random.choice(plage_id_playlist)
            id_morceau = random.choice(plage_id_morceau)
            combinaison = (id_playlist, id_morceau)
            if combinaison not in combinaisons_deja_generees:
                combinaisons_deja_generees.add(combinaison)
                break

        ligne_sql = f"({id_playlist}, {id_morceau})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_lignes:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour PlaylistMorceau ont été écrites dans {fichier_playlist_morceau}")
