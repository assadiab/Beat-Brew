# Projet BeatBrew Database

Ce projet est une base de données relationelle conçue pour gérer diverses entités et relations liées à un réseau social, BeatBrew, centré sur le musique.
Il permettra à ses utilisateurs de découvrir de nouveaux sons, d'aller à des concerts,d'emettre des avis/notes, de partagers des photos/vidéos, d'avoir des relations de followers et amis, de creer des playlist et de faire des publications.

Il inclut des scripts pour générer des données fictives, leus insertions dans la database , des scripts d'execution autimatiques et des scripts convertissants des fichiers SQL en CSV et Excel.

## Fonctionnalités
Ce projet contient les scripts suivants : 

- [beat_brew.sql](beat_brew.sql) : Script SQL principal pour créer et intialiser la base de données BeatBrew avec ses tables et contraintes.
- [requests_beat_brew.sql](requests_beat_brew.sql) : Script SQL contenant des requetes prédéfinies pour différentes manipulations des données.
- [data_script](data_script) : Dossiers de scripts générant des données fictives (sous formes de tables SQL) enregistrées dans un fichier de sortie sql
- [run_scripts.sh](run_scripts.sh) : Parcourt un dossier (ici data_script) et execute tous les scripts python qu'il contient puis déplace les fichiers SQL générés dans un dossier de sortie spécifié.
- [add_data.py](add_data.py) : Ajoute les données de fichiers SQL d'un dossier dans un fichier de sortie SQL existant spécifié.
- [sql_to_csv.py](asql_to_csv.py) : Convertit des fichiers SQL d'un dossier en fichiers CSV puis les stockent dans un dossier de sortie spécifié.
- [sql_to_excel.py](sql_to_excel.py) : Convertit des fichiers SQL d'un dossier en un fichier Excel avec chaque table sur une feuille distincte.

## Utilisation

Pour utiliser ces programmes, suivez les instructions ci-dessous :

### Étape 1 : Arborescence

Tout d'abord, assurez-vous de télécharger les fichiers nécessaires pour exécuter les programmes.
Vous aurez également besoin de savoir naviguer dans l'arborescence.

Assurez-vous d'avoir tous les fichiers necessaires dans votre répértoire en lancant la commande `ls`, vous devez obtenir la sortie suivante :
```bash
$ ls
chaos_game.py  clustering.py  genomes  genomic_sign.py
```






