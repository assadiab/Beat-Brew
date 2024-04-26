from faker import Faker
import random

fake = Faker()

# Nombre de relations à générer
nombre_relations = 100

# Nom du fichier SQL pour Relation
fichier_relation = "donnees_relation_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_relation, "w") as fichier:

    # Écrire l'en-tête SQL
    fichier.write("INSERT INTO Relation (Relation_ID, User1) VALUES\n")

    # Générer et écrire les lignes SQL
    for i in range(1, nombre_relations + 1):
        relation_id = i
        user1 = random.randint(1, 140)


        ligne_sql = f"({relation_id}, {user1})"

        # Ajouter une virgule à toutes les lignes sauf la dernière
        if i < nombre_relations:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        # Écrire la ligne dans le fichier
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Relation ont été écrites dans {fichier_relation}")
