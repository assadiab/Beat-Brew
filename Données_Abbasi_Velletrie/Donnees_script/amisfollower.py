from faker import Faker
import random

fake = Faker()

# Nombre de relations à générer
nombre_relations = 99

# Plage d'ID_Utilisateur 
plage_id_utilisateur = list(range(1, 151))

# Nom du fichier SQL pour Follower
fichier_follower = "donnees_follower_fictives.sql"

with open(fichier_follower, "w") as fichier:

    fichier.write("INSERT INTO Follower (Utilisateur_Id, Relation_ID) VALUES\n")

    for i in range(1, nombre_relations + 1):
        utilisateur_id = random.choice(plage_id_utilisateur)
        relation_id = i

        ligne_sql = f"({utilisateur_id}, {relation_id})"

        if i < nombre_relations:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Follower ont été écrites dans {fichier_follower}")

# Nom du fichier SQL pour Amis
fichier_amis = "donnees_amis_fictives.sql"

# Ouvrir le fichier en mode écriture
with open(fichier_amis, "w") as fichier:

    fichier.write("INSERT INTO Amis (Utilisateur_Id, Relation_ID) VALUES\n")

    for i in range(1, nombre_relations + 1):
        utilisateur_id = random.choice(plage_id_utilisateur)
        relation_id = i

        ligne_sql = f"({utilisateur_id}, {relation_id})"

        if i < nombre_relations:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne

        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Amis ont été écrites dans {fichier_amis}")
