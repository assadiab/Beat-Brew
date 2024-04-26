#!/bin/bash

# Créer un sous-dossier pour les sorties SQL s'il n'existe pas
mkdir -p output_sql

# Parcourir tous les fichiers Python dans le répertoire actuel
for script in *.py; do
    # Vérifier si le fichier est un script Python
    if [[ -f "$script" && "${script: -3}" == ".py" ]]; then
        # Récupérer le nom du fichier sans l'extension
        filename=$(basename -- "$script")
        filename_without_extension="${filename%.*}"
        # Exécuter le script Python
        python3 "$script"
    fi
done

# Parcourir tous les fichiers SQL dans le répertoire de travail
for sql_file in *.sql; do
    # Vérifier si le fichier est un fichier SQL
    if [[ -f "$sql_file" && "${sql_file: -4}" == ".sql" ]]; then
        # Déplacer le fichier SQL dans le dossier de sortie
        mv "$sql_file" output_sql/
    fi
done

echo "Tous les scripts Python ont été exécutés et les fichiers SQL ont été déplacés dans output_sql."
