from faker import Faker
import random

fake = Faker()

# Nombre de lignes à générer
nombre_lignes = 150

# Nom du fichier SQL pour Suggestion
fichier_suggestion = "donnees_suggestion_fictives.sql"

# Générer les données pour Suggestion
with open(fichier_suggestion, "w") as fichier:
    fichier.write("INSERT INTO Suggestion (Suggestion_ID, Type, Date) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        suggestion_id = i
        suggestion_type = random.choice([
            "Suggestion Ami",
            "Suggestion de Contenu",
            "Suggestion de Groupe",
            "Suggestion de Playlist",
            "Suggestion musicale",
            "Suggestion amis en fonction des intérêts communs",
            "Suggestion de groupes en fonction des genres musicaux préférés",
            "Suggestion amis basée sur des amis communs",
            "Suggestion de groupes basée sur des membres amis",
            "Suggestion de contenu basée sur les publications précédentes",
            "Suggestion de playlists basée sur les habitudes écoute",
            "Suggestion événement/concert basée sur les préférences musicales",
            "Suggestion de groupes participant à des événements"
        ])
        date = fake.date_this_decade().strftime("%Y-%m-%d")
        ligne_sql = f"({suggestion_id}, '{suggestion_type}', '{date}')"
        if i < nombre_lignes:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Suggestion ont été écrites dans {fichier_suggestion}")
