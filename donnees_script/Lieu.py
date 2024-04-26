from faker import Faker

fake = Faker()

# Nombre de lieux à générer
nombre_lieux = 10

# Plage d'ID d'avis de 1 à 71
plage_id_avis = list(range(1, 72))

# Nom du fichier SQL pour Lieu
fichier_lieu = "donnees_lieu_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_lieu, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Lieu (Lieu_ID, Nom, Adresse, Avis_ID) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_lieux + 1):
        lieu_id = i
        nom_lieu = fake.company().replace("'", "''")
        adresse_lieu = fake.address().replace("'", "''")
        avis_id = fake.random_element(plage_id_avis)

        ligne_sql = f"({lieu_id}, '{nom_lieu}', '{adresse_lieu}', {avis_id})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_lieux:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Lieu ont été écrites dans {fichier_lieu}")
