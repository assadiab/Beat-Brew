from faker import Faker
import random

fake = Faker()

# Plages d'ID pour les autres tables
plage_id_morceau = list(range(1, 101))  
plage_id_avis = list(range(1, 71)) 

# Nombre de lignes à générer
nombre_lignes = 30  

# Générer les données pour Avis_Morceau
with open("avis_morceau.sql", "w") as fichier:
    fichier.write("INSERT INTO Avis_Morceau (Avis_Id, Morceau_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        avis_id = random.choice(plage_id_avis)
        morceau_id = random.choice(plage_id_morceau)
        ligne_sql = f"({avis_id}, {morceau_id})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

print("Les données fictives pour la table Avis_Morceau a été écrites.")
