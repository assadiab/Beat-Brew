from faker import Faker
import random

fake = Faker()

# Nombre d'avis à générer
nombre_avis = 70

# Plage d'ID_Utilisateur de 1 à 150
plage_id_utilisateur = list(range(1, 151))

# Nom du fichier SQL pour Avis
fichier_avis = "donnees_avis_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_avis, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Avis (ID, Note, Commentaire, Pseudo, Date, Tags) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_avis + 1):
        id_avis = i
        note_avis = random.randint(0, 10)
        commentaire_avis = fake.text()
        pseudo_avis = fake.user_name()
        date_avis = fake.date_this_decade().strftime("%Y-%m-%d")
        tags_avis = fake.word()

        ligne_sql = f"({id_avis}, {note_avis}, '{commentaire_avis}', '{pseudo_avis}', '{date_avis}', '{tags_avis}')"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_avis:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Avis ont été écrites dans {fichier_avis}")
