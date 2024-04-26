import os
import sys

def add_sql_data_to_file(input_folder, output_file):
    # Vérifier si le fichier de sortie existe
    if not os.path.isfile(output_file):
        print("Le fichier de sortie spécifié n'existe pas.")
        sys.exit(1)

    # Ouvrir le fichier de sortie en mode lecture pour lire son contenu
    with open(output_file, "r") as target_sql_file:
        target_sql_content = target_sql_file.readlines()

    # Liste des fichiers SQL dans le dossier spécifié
    sql_files = [file for file in os.listdir(input_folder) if file.endswith(".sql")]

    # Ouvrir le fichier de sortie en mode ajout
    with open(output_file, "a") as output_sql_file:
        for sql_file in sql_files:
            # Chemin complet du fichier SQL
            sql_file_path = os.path.join(input_folder, sql_file)
            
            # Vérifier si le fichier contient des données
            with open(sql_file_path, "r") as file:
                if file.read().strip():
                    # Lire le contenu du fichier SQL
                    with open(sql_file_path, "r") as sql_content:
                        lines = sql_content.readlines()
                        
                        # Extraire le nom de la table à partir de la première ligne contenant "INSERT INTO"
                        table_name = None
                        for line in lines:
                            if "INSERT INTO" in line:
                                table_name = line.split("INSERT INTO")[1].split("(")[0].strip()
                                break

                        # Ajouter une ligne de commentaire formatée avant l'insertion de données
                        if table_name:
                            output_sql_file.write("\n-- {}\n".format(table_name))
                        else:
                            print("Impossible de déterminer le nom de la table dans le fichier {}.".format(sql_file))

                        # Ajouter le contenu du fichier SQL au fichier de sortie
                        output_sql_file.writelines(lines)

                        print("Les données du fichier {} ont été ajoutées à {}.".format(sql_file, output_file))
                else:
                    print("Le fichier {} est vide, aucune donnée à ajouter.".format(sql_file))

    print("Toutes les données ont été ajoutées à {}.".format(output_file))

if __name__ == "__main__":
    # Vérifier si le nombre d'arguments est correct
    if len(sys.argv) != 3:
        print("Utilisation: python add_sql_data_to_file.py <dossier_contenant_fichiers_sql> <fichier_sql_sortie>")
        sys.exit(1)

    # Récupérer les noms des dossiers et fichiers en ligne de commande
    input_folder = sys.argv[1]
    output_file = sys.argv[2]

    # Vérifier si le dossier d'entrée existe
    if not os.path.isdir(input_folder):
        print("Le dossier spécifié n'existe pas.")
        sys.exit(1)

    # Appeler la fonction pour ajouter les données SQL au fichier de sortie
    add_sql_data_to_file(input_folder, output_file)

