from faker import Faker
import random

fake = Faker()

# Nombre d'utilisateurs à générer
nombre_utilisateurs = 150

# Plages d'ID pour les références
plage_id_historique = list(range(1, 301))
plage_id_publication = list(range(0, 250))
plage_id_association = list(range(100, 111))
plage_id_personne = list(range(1, 61))
plage_id_lieu = list(range(1, 11))
plage_id_artistes = list(range(1, 101))
plage_id_playlist = list(range(1, 31))

# Nom du fichier SQL pour Utilisateur
fichier_utilisateur = "donnees_utilisateur_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_utilisateur, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Utilisateur (Utilisateur_ID, Pseudo, Email, Password, Biographie, Date_inscription, Historique_Id, Publication_Id, Association_Id, Personne_Id, Lieu_Id, Artistes_Id, Playlist_Id) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_utilisateurs + 1):
        utilisateur_id = i
        pseudo = fake.user_name()
        email = fake.email()
        password = fake.password()
        biographie = fake.text()
        date_inscription = fake.date_between(start_date='-365d', end_date='today').strftime('%Y-%m-%d')
        historique_id = random.choice(plage_id_historique)
        publication_id = random.choice(plage_id_publication)
        association_id = random.choice(plage_id_association)
        personne_id = random.choice(plage_id_personne)
        lieu_id = random.choice(plage_id_lieu)
        artistes_id = random.choice(plage_id_artistes)
        playlist_id = random.choice(plage_id_playlist)

        ligne_sql = f"({utilisateur_id}, '{pseudo}', '{email}', '{password}', '{biographie}', '{date_inscription}', {historique_id}, {publication_id}, {association_id}, {personne_id}, {lieu_id}, {artistes_id}, {playlist_id})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_utilisateurs:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Utilisateur ont été écrites dans {fichier_utilisateur}")
