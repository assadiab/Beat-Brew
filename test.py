import pandas as pd

# Les données extraites du fichier SQL
donnees = [
    (1, 'Knight-Huffman', 'KPop', 4),
    (2, 'Fischer Group', 'Classical', 7),
    (3, 'Martin, Lewis and Peterson', 'Rap', 10),
    (4, 'Joyce-Smith', 'Metal', 4),
    (5, 'Stevens, Anthony and Robinson', 'Country', 4),
    (6, 'Flowers-Butler', 'Blues', 6),
    (7, 'Howard-Jones', 'Jazz', 5),
    (8, 'Dickerson, Wilson and Martin', 'Hip-hop', 3),
    (9, 'Lewis Ltd', 'Electronic', 5),
    (10, 'Martin, Flowers and Henry', 'Rock', 4),
    (100, 'Serrano, Austin and Powell', 'Classical', 6)
]

# Créer un DataFrame Pandas à partir des données
df = pd.DataFrame(donnees, columns=["Artistes_ID", "Nom", "Genre", "Nb_Membres"])

# Exporter le DataFrame vers un fichier Excel
chemin_fichier_excel = "artistes.xlsx"  # Spécifiez le chemin du fichier Excel de sortie
df.to_excel(chemin_fichier_excel, index=False)

print("Les données ont été exportées avec succès vers", chemin_fichier_excel)
