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
        # Exécuter le script Python et rediriger la sortie vers un fichier SQL dans output_sql
        python3 "$script" > "output_sql/${filename_without_extension}.sql"
        echo "Le fichier SQL ${filename_without_extension}.sql a été généré dans output_sql."
    fi
done

echo "Tous les scripts Python ont été exécutés et leurs sorties ont été enregistrées dans output_sql."

