from faker import Faker
import random

fake = Faker()

# Nombre de lignes à générer
nombre_lignes = 300

# Nom du fichier SQL pour Historique
fichier_historique = "donnees_historique_fictives.sql"

# Générer les données pour Historique
with open(fichier_historique, "w") as fichier:
    fichier.write("INSERT INTO Historique (Historique_ID, Type, Date) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        historique_id = i
        date = fake.date_this_decade().strftime("%Y-%m-%d")
        type_historique = random.choice(['Connexion', 'Déconnexion', 'Modification de Profil', 'Création', 'Lecture', 'Mise à Jour', 'Suppression', 'Ajout Ami', 'Suppression Ami', 'Abonnement', 'Désabonnement', 'Publication', 'Modification de Publication', 'Suppression de Publication', 'Commentaire', 'Like', 'Partage', 'Création de Groupe', 'Rejoindre un Groupe', 'Quitter un Groupe', 'Envoi de Message Privé', 'Réception de Message Privé', 'Lecture de Message Privé', 'Création de Playlist', 'Modification de Playlist', 'Suppression de Playlist'])
        ligne_sql = f"({historique_id}, '{type_historique}', '{date}')"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Historique ont été écrites dans {fichier_historique}")
