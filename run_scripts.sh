#!/bin/bash

# Vérifier si le nombre d'arguments est correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <dossier_contenant_fichiers>"
    exit 1
fi

# Récupérer le chemin complet du dossier spécifié
input_folder="$1"

# Chemin du dossier contenant le script
script_dir=$(dirname "${BASH_SOURCE[0]}")

# Créer un sous-dossier pour les sorties SQL s'il n'existe pas dans le dossier du script
mkdir -p "$script_dir/output_donnees_sql"

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
        mv "$sql_file" "./output_donnees_sql/"
    fi
done

echo "Tous les fichiers SQL ont été déplacés dans output_donnes_sql."


