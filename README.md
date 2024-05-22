# Projet BeatBrew Database

Ce projet est une base de données relationnelle conçue pour gérer diverses entités et relations liées à un réseau social, BeatBrew, centré sur la musique. Il permet à ses utilisateurs de découvrir de nouveaux sons, d'assister à des concerts, d'émettre des avis/notes, de partager des photos/vidéos, de gérer des relations de followers et d'amis, de créer des playlists et de faire des publications.

Il inclut des scripts pour générer des données fictives, les insérer dans la base de données, des scripts d'exécution automatique, et des scripts convertissant des fichiers SQL en CSV et Excel.

## Fonctionnalités

Ce projet contient les scripts suivants :

- **[beat_brew.sql](beat_brew.sql)** : Script SQL principal pour créer et initialiser la base de données BeatBrew avec ses tables et contraintes.
- **[requests_beat_brew.sql](requests_beat_brew.sql)** : Script SQL contenant des requêtes prédéfinies pour différentes manipulations des données.
- **data_script** : Dossier contenant des scripts générant des données fictives (sous forme de tables SQL) enregistrées dans un fichier de sortie SQL.
- **[run_scripts.sh](run_scripts.sh)** : Parcourt un dossier (ici `data_script`), exécute tous les scripts Python qu'il contient, puis déplace les fichiers SQL générés dans un dossier de sortie spécifié.
- **[add_data.py](add_data.py)** : Ajoute les données de fichiers SQL d'un dossier dans un fichier de sortie SQL existant spécifié.
- **[sql_to_csv.py](sql_to_csv.py)** : Convertit des fichiers SQL d'un dossier en fichiers CSV, puis les stocke dans un dossier de sortie spécifié.
- **[sql_to_excel.py](sql_to_excel.py)** : Convertit des fichiers SQL d'un dossier en un fichier Excel avec chaque table sur une feuille distincte.

## Utilisation

Ces programmes vous permettront d'alimenter votre modèle et d'organiser vos données générées sous différents formats pour une analyse a posteriori (sous PowerBI ou R). Pour utiliser ces programmes, suivez les instructions ci-dessous :

### Étape 1 : Arborescence

Tout d'abord, assurez-vous de télécharger les fichiers nécessaires pour exécuter les programmes et d'avoir un script SQL initialisant votre modèle.

- `data_script` contenant les scripts Python nécessaires à la génération de données fictives.
- `run_scripts.sh`
- `add_data.py`
- `sql_to_excel.py` et `sql_to_csv.py`

Vérifiez le contenu de votre répertoire en lançant la commande `ls`. Vous devez obtenir la sortie suivante (plus votre fichier SQL) :

```bash
$ ls
data_script      run_scripts.sh  add_data.py
sql_to_excel.py  sql_to_csv.py   
```

Pour vérifier le contenu d'un répertoire, utilisez la commande suivante (`./` signifie que vous êtes dans le répertoire actuel). Prenons l'exemple du répertoire `data_script` :

```bash
$ ls ./data_script 
Annonce.py       Interet.py    amisfollower.py  concert.py     personne.py         suggestion.py   utilisateur.py
Archive.py       Lieu.py       asso.py          historique.py  playlist.py         tag.py
Artistes.py      Participe.py  avis.py          message.py     playlistmorceau.py  tag_FK.py
Avis_morceau.py  Relation.py   avis_artiste.py  morceau.py     publication.py      uti_sugg_mp.py
```

### Étape 2 : Exécution des programmes

Pour utiliser ces programmes, exécutez les commandes suivantes dans votre terminal :

- **`run_scripts.sh`** : Génère le dossier de fichiers SQL ou prend un dossier existant.

```bash
$ ./run_scripts.sh <dossier_script_python> <dossier_sortie_sql>
```

- **`add_data.py`** : Le fichier SQL de sortie doit être existant (nous n'ajoutons que les tables, la structure du modèle doit être définie).

```bash
$ python3 add_data.py <dossier_contenant_fichiers_sql> <fichier_sql_sortie>
```

- **`sql_to_excel.py`** : Génère le fichier Excel de sortie (utilisez l'extension `.xlsx`).

```bash
$ python3 sql_to_excel.py <input_sql_folder> <output_excel_file>
```

- **`sql_to_csv.py`** : Génère le dossier de fichiers CSV ou prend un dossier existant.

```bash
$ python3 sql_to_csv.py <input_sql_folder> <output_csv_folder>
```

## Exemples d'utilisation

### Exemple 1 : `run_scripts.sh`

Nous utilisons le dossier de scripts Python `data_script`.

```bash
$ ./run_scripts.sh data_script data_sql
```

Vous obtiendrez :

```bash
Les données fictives pour Annonce_Concert ont été écrites dans donnees_annonce_concert_fictives.sql
Les données fictives pour Archive ont été écrites dans donnees_archive_fictives.sql
...
Tous les scripts Python du dossier data_script ont été exécutés.
Tous les fichiers SQL sont dans le dossier data_sql.
```

### Exemple 2 : `add_data.py`

```bash
$ python3 add_data.py data_sql beat_brew.sql
```

Vous obtiendrez :

```bash
Toutes les données ont été ajoutées à beat_brew.sql.
```

Si le fichier SQL fourni n'existe pas, une erreur se produira. Voici le message d'avertissement :

```bash
Le fichier de sortie spécifié n'existe pas.
```

### Exemple 3 : `sql_to_excel.py`

```bash
$ python3 sql_to_excel.py data_sql data.xlsx
```

Vous obtiendrez :

```bash
Toutes les données SQL ont été exportées dans data.xlsx
```

### Exemple 4 : `sql_to_csv.py`

```bash
$ python3 sql_to_csv.py data_sql data_csv
```

Vous obtiendrez :

```bash
Conversion des fichiers terminée. CSV sauvegardés dans le dossier data_csv
```
