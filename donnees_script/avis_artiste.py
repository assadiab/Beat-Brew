from faker import Faker
import random

fake = Faker()

# Plages d'ID pour les autres tables
plage_id_artistes = list(range(1, 31))
plage_id_avis = list(range(1, 71))  

# Nombre de lignes à générer
nombre_lignes = 30  

# Générer les données pour Avis_Artiste
with open("avis_artiste.sql", "w") as fichier:
    fichier.write("INSERT INTO Avis_Artiste (Avis_Id, Artistes_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        avis_id = random.choice(plage_id_avis)
        artistes_id = random.choice(plage_id_artistes)
        ligne_sql = f"({avis_id}, {artistes_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        else:
            ligne_sql += ";"  # Ajouter le ";" à la dernière ligne
        fichier.write(f"{ligne_sql}\n")

print("Les données fictives pour la table Avis_Artistes a été écrite.")