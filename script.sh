#!/bin/bash

# Vérifier le nombre d'arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 dossier_sql dossier_excel"
    exit 1
fi

# Récupérer les dossiers d'entrée et de sortie
dossier_sql="$1"
dossier_excel="$2"

# Vérifier si les dossiers existent
if [ ! -d "$dossier_sql" ]; then
    echo "Le dossier SQL '$dossier_sql' n'existe pas."
    exit 1
fi

# Créer le dossier de sortie s'il n'existe pas
if [ ! -d "$dossier_excel" ]; then
    mkdir -p "$dossier_excel"
fi

# Parcourir tous les fichiers dans le dossier SQL
for fichier_sql in "$dossier_sql"/*.sql; do
    if [ -f "$fichier_sql" ]; then
        nom_fichier_excel=$(basename "$fichier_sql" .sql).xlsx
        
        # Extraire les données du fichier SQL
        donnees=$(grep -oP "(?<=VALUES \().*(?=\))" "$fichier_sql")
        
        # Créer un DataFrame Pandas à partir des données
        echo "$donnees" > temp.txt
        python3 sql_to_excel.py temp.txt "$dossier_excel/$nom_fichier_excel"
        rm temp.txt
    fi
done

echo "Conversion des fichiers SQL en fichiers Excel terminée."

