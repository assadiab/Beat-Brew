"""
Nom du fichier : sql_to_csv.py
Description : Ce script convertit des fichiers SQL d'un dossier en fichiers CSV puis les stockent dans un dossier de sortie spécifié.
Auteur : Assa DIABIRA
Dernière modification : 27/04/2024
"""

import os
import pandas as pd
import re
import csv
import sys

def split_commas(text):
    # Split personnalisé prenant en compte les virgules entre guillemets simples
    result = []
    in_quotes = False
    current_field = ''
    for char in text:
        if char == ',' and not in_quotes:
            result.append(current_field)
            current_field = ''
        else:
            current_field += char
            if char == "'":
                in_quotes = not in_quotes
    result.append(current_field)
    return result

def sql_to_csv(input_sql_folder, output_csv_folder):
    # Vérifier si le répertoire de sortie existe, sinon le créer
    if not os.path.exists(output_csv_folder):
        os.makedirs(output_csv_folder)

    # Parcourir tous les fichiers SQL dans le répertoire d'entrée
    for filename in os.listdir(input_sql_folder):
        if filename.endswith(".sql"):
            input_sql_file = os.path.join(input_sql_folder, filename)
            output_csv_file = os.path.join(output_csv_folder, os.path.splitext(filename)[0] + ".csv")
            
            with open(input_sql_file, 'r') as file:
                sql_query = file.read()

            # Recherche des valeurs entre parenthèses
            data = re.findall(r'\((.*?)\)', sql_query)

            # Séparation des valeurs et suppression des espaces
            data_lines = [line.strip() for line in data]

            # Traitement des valeurs et création des lignes de données pour le CSV
            csv_data = []
            for line in data_lines:
                fields = split_commas(line)
                csv_data.append(fields)

            # Création du fichier CSV avec un délimiteur de virgule
            with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',')
                csv_writer.writerows(csv_data)

    print(f"Conversion des fichiers terminée. CSV sauvegardés dans le dossier {output_csv_folder} .")

# Utilisation : python3 sql_to_csv.py input_sql_folder output_csv_folder
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python sql_to_csv.py input_sql_folder output_csv_folder")
        sys.exit(1)

    input_sql_folder = sys.argv[1]
    output_csv_folder = sys.argv[2]
    sql_to_csv(input_sql_folder, output_csv_folder)

