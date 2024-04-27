"""
Script : csv_to_excel.py
Description : Ce script prend en entrée un dossier contenant des fichiers CSV, les convertit en un fichier Excel avec chaque table sur une feuille séparée.
Auteur : Assa DIABIRA
Dernière modification : 27/04/2024
"""

import os
import pandas as pd
import sys

def csv_to_excel(input_folder, output_file):
    # Créer un writer Excel pour écrire dans le fichier de sortie
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    
    # Parcourir tous les fichiers CSV dans le dossier spécifié
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            # Lire le contenu du fichier CSV dans une DataFrame pandas
            df = pd.read_csv(file_path)
            # Extraire le nom de la table à partir du nom du fichier CSV (sans l'extension)
            table_name = os.path.splitext(filename)[0][:31]  # Tronquer le nom à 31 caractères
            # Écrire la DataFrame dans une feuille de calcul Excel avec le nom de la table comme nom de la feuille
            df.to_excel(writer, sheet_name=table_name, index=False)

    # Sauvegarder et fermer le fichier Excel
    writer.close()

    print(f"Toutes les tables ont été exportées dans {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_folder output_file.xlsx")
        sys.exit(1)

    input_folder = sys.argv[1]  # Chemin vers le dossier contenant les fichiers SQL
    output_file = sys.argv[2]   # Chemin vers le fichier Excel de sortie
    csv_to_excel(input_folder, output_file)

