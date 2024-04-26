from faker import Faker
import random

fake = Faker()

# Nombre de lignes à générer
nombre_lignes = 150

# Plages d'ID_Utilisateur et ID_Message_Prive
plage_id_utilisateur = list(range(1, 151))
plage_id_message_prive = list(range(1, 151))

# Plages d'ID_Suggestion
plage_id_suggestion = list(range(1, 51))

# Nom des fichiers SQL
fichier_uti_mp = "donnees_uti_mp_fictives.sql"
fichier_uti_sugg = "donnees_uti_sugg_fictives.sql"

# Générer les données pour Uti_MP
with open(fichier_uti_mp, "w") as fichier:
    fichier.write("INSERT INTO Uti_MP (Utilisateur_Id, Message_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        id_utilisateur = random.choice(plage_id_utilisateur)
        id_message_prive = random.choice(plage_id_message_prive)
        ligne_sql = f"({id_utilisateur}, {id_message_prive})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Uti_MP ont été écrites dans {fichier_uti_mp}")

# Générer les données pour Uti_Sugg
with open(fichier_uti_sugg, "w") as fichier:
    fichier.write("INSERT INTO Uti_Sugg (Utilisateur_Id, Suggestion_ID) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        id_utilisateur = random.choice(plage_id_utilisateur)
        id_suggestion = random.choice(plage_id_suggestion)
        ligne_sql = f"({id_utilisateur}, {id_suggestion})"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Uti_Sugg ont été écrites dans {fichier_uti_sugg}")
