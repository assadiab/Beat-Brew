import pandas as pd
import sys

def main():
    # Lire les données depuis l'entrée standard (stdin)
    data = sys.stdin.read().strip()
    
    # Diviser les données en lignes
    rows = [row.strip() for row in data.split('),(')]

    # Diviser chaque ligne en colonnes et supprimer les parenthèses
    rows = [row[1:-1].split(',') for row in rows]

    # Créer un DataFrame Pandas à partir des données
    df = pd.DataFrame(rows)

    # Spécifier le chemin du fichier Excel de sortie
    output_file = sys.argv[1]

    # Exporter le DataFrame vers un fichier Excel
    df.to_excel(output_file, index=False, header=False)

if __name__ == "__main__":
    main()
