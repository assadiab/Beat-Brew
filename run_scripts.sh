#!/bin/bash

# Nom du fichier : run_scripts.sh
# Description : Ce script parcourt un dossier spécifié, exécute tous les scripts Python qu'il contient, puis déplace tous les fichiers SQL générés dans un dossier de sortie.
# Auteur : Assa DIABIRA
# Dernière modification : 27/04/2024

# Vérifier si le nombre d'arguments est correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <dossier_contenant_fichiers> <dossier_sortie_sql>"
    exit 1
fi

# Récupérer le chemin complet du dossier spécifié
input_folder="$1"
output_folder="$2"

# Chemin du dossier contenant le script
script_dir=$(dirname "${BASH_SOURCE[0]}")

# Créer un sous-dossier pour les sorties SQL s'il n'existe pas dans le dossier du script
mkdir -p "$output_folder"

# Parcourir tous les fichiers Python dans le dossier spécifié
for script in "$input_folder"/*.py; do
    # Vérifier si le fichier est un script Python
    if [[ -f "$script" && "${script: -3}" == ".py" ]]; then
        # Récupérer le nom du fichier sans l'extension
        filename=$(basename -- "$script")
        filename_without_extension="${filename%.*}"
        # Exécuter le script Python
        python3 "$script"
    fi
done

echo "Tous les scripts Python du dossier $input_folder ont été exécutés."

# Parcourir tous les fichiers SQL dans le dossier spécifié
for sql_file in "$script_dir"/*.sql; do
    # Vérifier si le fichier est un fichier SQL
    if [[ -f "$sql_file" && "${sql_file: -4}" == ".sql" ]]; then
        # Déplacer le fichier SQL dans le dossier de sortie
        mv "$sql_file" "$output_folder"
    fi
done
echo "Tous les fichiers sql sont dans le dossier $output_folder."


