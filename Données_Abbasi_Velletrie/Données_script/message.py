from faker import Faker
import random

fake = Faker()

# Nombre de lignes à générer
nombre_lignes = 150

# Nom du fichier SQL pour Message_Prive
fichier_message_prive = "donnees_message_prive_fictives.sql"

# Générer les données pour Message_Prive
with open(fichier_message_prive, "w") as fichier:
    fichier.write("INSERT INTO Message_Prive (Message_ID, Destinataire_pseudo, Contenu, Date, Etat) VALUES\n")
    for i in range(1, nombre_lignes + 1):
        message_id = i
        destinataire_pseudo = fake.user_name()
        contenu = fake.text()
        date = fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
        etat = random.choice(['distribue', 'lu'])
        ligne_sql = f"({message_id}, '{destinataire_pseudo}', '{contenu}', '{date}', '{etat}')"
        if i < nombre_lignes:
            ligne_sql += ","
        fichier.write(f"{ligne_sql}\n")

print(f"Les données fictives pour Message_Prive ont été écrites dans {fichier_message_prive}")
