from faker import Faker

fake = Faker()

# Nombre d'associations à générer
nombre_associations = 11  # de 100 à 110 inclus

# Nom du fichier SQL pour Association
fichier_association = "donnees_association_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_association, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Association (Association_ID, Nom, Site_web) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(100, 100 + nombre_associations):
        association_id = i
        nom_association = fake.company().replace("'", "''")
        site_web = fake.url()

        ligne_sql = f"({association_id}, '{nom_association}', '{site_web}')"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < 100 + nombre_associations - 1:
            ligne_sql += ","

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Association ont été écrites dans {fichier_association}")
