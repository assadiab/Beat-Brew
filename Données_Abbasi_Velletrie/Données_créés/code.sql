-- Database: Music

-- DROP DATABASE IF EXISTS "Music";

CREATE DATABASE "Music"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	CREATE DATABASE "BDD_musique"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
--DROP TABLE Historique;
	CREATE TABLE Historique (
    Historique_ID INTEGER PRIMARY KEY,
    Type VARCHAR(100) NOT NULL CHECK (Type IN ('Connexion', 'Déconnexion', 'Modification de Profil', 'Création', 'Lecture', 'Mise à Jour', 'Suppression', 'Ajout d''Ami', 'Suppression d''Ami', 'Abonnement', 'Désabonnement', 'Publication', 'Modification de Publication', 'Suppression de Publication', 'Commentaire', 'Like', 'Partage', 'Création de Groupe', 'Rejoindre un Groupe', 'Quitter un Groupe', 'Envoi de Message Privé', 'Réception de Message Privé', 'Lecture de Message Privé', 'Création de Playlist', 'Modification de Playlist', 'Suppression de Playlist')),
    Date DATE NOT NULL
);
SELECT * FROM Historique;

-- DROP TABLE Publication;
CREATE TABLE Publication (
  Publication_ID INTEGER PRIMARY KEY,
  Date DATE NOT NULL
);
SELECT * FROM Publication

-- DROP TABLE Suggestions;
CREATE TABLE Suggestions (
  Id INTEGER PRIMARY KEY,
  Utilisateur_Id INTEGER REFERENCES Utilisateur(Utilisateur_Id),
  Type VARCHAR(50),
  Date DATE
);
SELECT * FROM Suggestions

-- DROP TABLE Message_Prive;
CREATE TABLE Message_Prive (
    Message_ID INTEGER PRIMARY KEY,
    Destinataire_pseudo VARCHAR(50),
    Contenu TEXT,
    Date TIMESTAMP,
    Etat VARCHAR(10) CHECK (Etat IN ('distribue', 'lu'))
);
SELECT * FROM Message_Prive

-- DROP TABLE Suggestions; 
CREATE TABLE Suggestion (
  Suggestion_ID INTEGER PRIMARY KEY,
  Type VARCHAR(50) CHECK (Type IN (
    'Suggestion Ami',
    'Suggestion de Contenu',
    'Suggestion de Groupe',
    'Suggestion de Playlist',
    'Suggestion musicale',
    'Suggestion amis en fonction des intérêts communs',
    'Suggestion de groupes en fonction des genres musicaux préférés',
    'Suggestion amis basée sur des amis communs',
    'Suggestion de groupes basée sur des membres amis',
    'Suggestion de contenu basée sur les publications précédentes',
    'Suggestion de playlists basée sur les habitudes écoute',
    'Suggestion événement/concert basée sur les préférences musicales',
    'Suggestion de groupes participant à des événements'
  )),
  Date DATE
);

SELECT * FROM Suggestion;

-- DROP TABLE Personne; 
CREATE TABLE Personne (
  Personne_ID INTEGER PRIMARY KEY REFERENCES Utilisateur(Utilisateur_ID),
  Age INTEGER,
  Genre CHAR(1),
  Nationnalite VARCHAR(100)
);
SELECT * FROM Personne;

-- DROP TABLE Groupe; 
CREATE TABLE Groupe (
  Groupe_ID INTEGER PRIMARY KEY REFERENCES Utilisateur(Utilisateur_ID),
  Nom VARCHAR(100),
  Genre VARCHAR(100), 
  Nb_Membres INTEGER
);
SELECT * FROM Groupe;

-- DROP TABLE Association; 
CREATE TABLE Association (
  Association_ID INTEGER PRIMARY KEY REFERENCES Utilisateur(Utilisateur_ID),
  Nom VARCHAR(100),
  Site_web VARCHAR(200)
);
SELECT * FROM Association;

-- DROP TABLE Lieu; 
CREATE TABLE Lieu (
  Lieu_ID INTEGER PRIMARY KEY,
  Nom VARCHAR(100) NOT NULL,
  Adresse TEXT UNIQUE NOT NULL
);

SELECT * FROM Lieu;

-- DROP TABLE SalleC; 
CREATE TABLE SalleC (
    SalleC_ID INTEGER PRIMARY KEY REFERENCES Utilisateur(Utilisateur_ID),
    Nom VARCHAR(100),
    Capacite INTEGER,
	ID_Lieu INTEGER REFERENCES Lieu(Lieu_ID)
);
SELECT * FROM SalleC;

-- DROP TABLE Relation; 
CREATE TABLE Relation(
  Relation_ID INTEGER PRIMARY KEY,
  User1 INTEGER REFERENCES Utilisateur(Utilisateur_Id),
  User2 INTEGER REFERENCES Utilisateur(Utilisateur_Id),
  Status VARCHAR(50) CHECK (Status IN ('Suivi', 'Ami', 'Abonné')),
  CHECK (User1 <> User2)
);
SELECT * FROM Relation_Amitie;

-- DROP TABLE Concert;
CREATE TABLE Concert (
  Concert_Id INTEGER PRIMARY KEY,
  Nom VARCHAR(60),
  Date DATE,
  Organisateurs VARCHAR(100),
  "Line-up" VARCHAR(255),
  Nombre_places INTEGER,
  Cause_soutien BOOLEAN,
  Espace_exterieur BOOLEAN, 
  Enfants_permis BOOLEAN,
  Prix DECIMAL(10, 2),
  Nb_volontaires INTEGER,
  ID_Lieu INTEGER REFERENCES Lieu(Lieu_ID)
);
SELECT * FROM Concert;

-- DROP TABLE Archive; 
CREATE TABLE Archive (
  Archive_Id INTEGER PRIMARY KEY,
  Concert_Id INTEGER REFERENCES Concert(Concert_Id),
  Date_archivage DATE,
  Nb_participants INTEGER,
  Avis_participants TEXT,
  Photo_path VARCHAR(255),
  Video_path VARCHAR(255)
);
SELECT * FROM Archive;

-- Créer une fonction pour vérifier la contrainte
CREATE OR REPLACE FUNCTION check_archive_date()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.Date_archivage < (SELECT "Date" FROM Concert WHERE Id = NEW.Concert_Id) THEN
    RAISE EXCEPTION 'Date_archivage must be greater than or equal to Concert."Date"';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Créer un déclencheur avant l'insertion dans CArchive
CREATE TRIGGER check_archive_date_trigger
BEFORE INSERT ON Archive
FOR EACH ROW EXECUTE FUNCTION check_archive_date();

-- Créer la table Participe avec une contrainte CHECK basée sur la fonction
-- DROP TABLE Participe
CREATE TABLE Participe (
  Concert_ID INTEGER REFERENCES Concert(Concert_ID),
  Personne_ID INTEGER REFERENCES Personne(Personne_ID),
  PRIMARY KEY (Concert_ID, Personne_ID)
);
SELECT * FROM Participe

-- DROP TABLE Interet;
CREATE TABLE Interet (
  Concert_ID INTEGER REFERENCES Concert(Concert_ID),
  Personne_ID INTEGER REFERENCES Personne(Personne_ID),
  PRIMARY KEY (Concert_ID, Personne_ID)
);
SELECT * FROM Interet

-- DROP TABLE Annonce_Concert;
CREATE TABLE Annonce_Concert (
  Annonce_Id INTEGER PRIMARY KEY,
  Utilisateur_Id INTEGER REFERENCES Utilisateur(Utilisateur_Id),
  Concert_Id INTEGER REFERENCES Concert(Concert_Id),
  Date_annonce DATE
);
SELECT * FROM Annonce_Concert

-- DROP TABLE Playlist;
CREATE TABLE Playlist (
  Playlist_Id VARCHAR(200) PRIMARY KEY,
  Nom VARCHAR(100),
  IsGroupe BOOLEAN,
  Utilisateur_Id INTEGER REFERENCES Utilisateur(Utilisateur_Id)
);
SELECT * FROM Playlist

-- DROP TABLE Morceau;
CREATE TABLE Morceau (
  Id VARCHAR(200) PRIMARY KEY,
  Titre VARCHAR(100),
  Nom_album VARCHAR(100),
  Genre VARCHAR(50)
);
SELECT * FROM Morceau 

-- DROP TABLE PlaylistMorceau;
CREATE TABLE PlaylistMorceau (
  Playlist_Id VARCHAR(200) REFERENCES Playlist(Id),
  Morceau_Id VARCHAR(200) REFERENCES Morceau(Id),
  PRIMARY KEY (Playlist_Id, Morceau_Id)
);
SELECT * FROM PlaylistMorceau

-- DROP TABLE Avis;
CREATE TABLE Avis (
  ID VARCHAR(200) PRIMARY KEY,
  Note INTEGER CHECK (Note >= 0 AND Note <= 10),
  Commentaire TEXT,
  Utilisateur_Id INTEGER REFERENCES Utilisateur(Id)
);
SELECT * FROM Avis


DROP TABLE Utilisateur;
CREATE TABLE Utilisateur (
    Utilisateur_ID INTEGER PRIMARY KEY,
    Pseudo VARCHAR(30),
    Email VARCHAR,
    Password VARCHAR,
    Biographie TEXT,
    Date_inscription DATE,
    Historique_Id INTEGER REFERENCES Historique(Historique_Id),
	Publication_Id INTEGER REFERENCES Publication(Publication_Id)
);
SELECT * FROM Utilisateur;


-- DROP TABLE Tag;
CREATE TABLE Tag (
  Id INTEGER PRIMARY KEY,
  Mot VARCHAR(100),
  Type VARCHAR(50) CHECK (Type IN ('Groupe', 'Avis', 'Concert', 'Playlist', 'Lieu')), 
  Id_Type VARCHAR(200)
);
SELECT * FROM Tag


