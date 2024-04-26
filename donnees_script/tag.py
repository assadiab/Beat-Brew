from faker import Faker

fake = Faker()

# Nombre de tags à générer
nombre_tags = 50

# Nom du fichier SQL pour Tag
fichier_tag = "donnees_tag_fictives.sql"

# Ensemble pour suivre les mots déjà générés
mots_generes = set()

# Ouvrir le fichier en mode écriture
with open(fichier_tag, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Tag (Id, Mot) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_tags + 1):
        tag_id = i
        mot_tag = fake.word()

        # S'assurer que le mot généré est unique
        while mot_tag in mots_generes:
            mot_tag = fake.word()

        mots_generes.add(mot_tag)

        ligne_sql = f"({tag_id}, '{mot_tag}')"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_tags:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Tag ont été écrites dans {fichier_tag}")
