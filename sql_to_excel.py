"""
Nom du fichier : sql_to_excel.py
Description : Ce script convertit des fichiers SQL d'un dossier en un fichier Excel avec chaque table sur une feuille séparée.
Auteur : Assa DIABIRA
Dernière modification : 27/04/2024
"""

import os
import pandas as pd
import re
import sys

def split_commas(text):
    # Fonction pour séparer les valeurs entre parenthèses par des virgules
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

def sql_to_excel(input_sql_folder, output_excel_file):
    # Créer un writer Excel pour écrire dans le fichier de sortie
    writer = pd.ExcelWriter(output_excel_file, engine='xlsxwriter')

    # Vérifier si le répertoire d'entrée existe
    if not os.path.exists(input_sql_folder):
        print("Le répertoire spécifié pour les fichiers SQL n'existe pas.")
        sys.exit(1)

    # Parcourir tous les fichiers SQL dans le répertoire d'entrée
    for filename in os.listdir(input_sql_folder):
        if filename.endswith(".sql"):
            input_sql_file = os.path.join(input_sql_folder, filename)
            
            with open(input_sql_file, 'r') as file:
                sql_query = file.read()

            # Recherche des noms de table dans le fichier SQL
            table_names = re.findall(r'INTO (\w+)', sql_query)

            # Recherche des valeurs entre parenthèses pour chaque table
            data = re.findall(r'\((.*?)\)', sql_query)

            # Séparation des valeurs et suppression des espaces
            data_lines = [line.strip() for line in data]

            # Traitement des valeurs et création des lignes de données pour chaque table
            for i, table_name in enumerate(table_names):
                excel_data = []
                for line in data_lines:
                    fields = split_commas(line)
                    excel_data.append(fields)

                # Créer une DataFrame pandas avec les données de la table
                df = pd.DataFrame(excel_data)

                # Écrire la DataFrame dans une page Excel avec le nom de la table comme titre de la page
                df.to_excel(writer, sheet_name=table_name, index=False, header=False)

    # Sauvegarder et fermer le fichier Excel
    writer.close()

    print(f"Toutes les données SQL ont été exportées dans {output_excel_file}")

# Utilisation : python3 sql_to_excel.py input_sql_folder output_excel_file
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python sql_to_excel.py input_sql_folder output_excel_file")
        sys.exit(1)

    input_sql_folder = sys.argv[1]
    output_excel_file = sys.argv[2]
    sql_to_excel(input_sql_folder, output_excel_file)

