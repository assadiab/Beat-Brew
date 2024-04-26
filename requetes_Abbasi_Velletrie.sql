-- PARTIE 3) Requetes 

-- #1 : Lister tous les concerts avec leur détails
SELECT Concert.*, Lieu.Nom AS Lieu_Nom, Lieu.Adresse AS Lieu_Adresse
FROM Concert
JOIN Lieu ON Concert.ID_Lieu = Lieu.Lieu_ID;

-- #2 : Afficher les utilisateurs et leurs playlists associées 
SELECT Utilisateur.Pseudo, Playlist.Nom AS Playlist_Nom
FROM Utilisateur
LEFT JOIN Playlist ON Utilisateur.Playlist_Id = Playlist.Playlist_ID;

-- #3 : Afficher les utilisateurs et leurs annonces de concerts associées
SELECT Concert.Nom AS Concert_Nom, Lieu.Nom AS Lieu_Nom
FROM Concert
INNER JOIN Lieu ON Concert.ID_Lieu = Lieu.Lieu_ID;

-- #4 : Récupérer les morceaux d'une playlist spécifique
SELECT Morceau.*
FROM Morceau
JOIN PlaylistMorceau ON Morceau.Morceau_Id = PlaylistMorceau.Morceau_Id
WHERE PlaylistMorceau.Playlist_Id = 4 ;

-- #5: Obtenir les lieux associés à un tag spécifique 
SELECT Lieu.*
FROM Lieu
JOIN Tag_Lieu ON Lieu.Lieu_ID = Tag_Lieu.Lieu_ID
WHERE Tag_Lieu.Tag_Id = 8;

-- #6 : renvoie les 5 concerts ayant le plus de participants
SELECT Concert.Concert_Id, Concert.Nom AS Nom_Concert, COUNT(Participe.Personne_ID) AS Nombre_Participants
FROM Concert
JOIN Participe ON Concert.Concert_Id = Participe.Concert_ID
GROUP BY Concert.Concert_Id, Concert.Nom
ORDER BY Nombre_Participants DESC
LIMIT 5;

-- #7 : Afficher les morceaux et les playlists auxquelles ils appartiennent
SELECT Morceau.Titre, Playlist.Nom AS Playlist_Nom
FROM Morceau
LEFT JOIN PlaylistMorceau ON Morceau.Morceau_Id = PlaylistMorceau.Morceau_Id
LEFT JOIN Playlist ON PlaylistMorceau.Playlist_Id = Playlist.Playlist_Id;

-- #8 : utilisateur qui ont créer des playlist de groupe
SELECT Utilisateur.Utilisateur_ID, Utilisateur.Pseudo, Playlist.Playlist_ID, Playlist.Nom AS Nom_Playlist
FROM Utilisateur
JOIN Playlist ON Utilisateur.Playlist_Id = Playlist.Playlist_ID
WHERE Playlist.IsGroupe;

-- #9 : Requetes sur au moins 3 tables : Renvoie une liste d'utilisateurs avec des infos sur leur historique/publications
SELECT Utilisateur.Pseudo, Historique.Type, Publication.Date AS Publication_Date
FROM Utilisateur
JOIN Historique ON Utilisateur.Historique_Id = Historique.Historique_ID
LEFT JOIN Publication ON Utilisateur.Publication_Id = Publication.Publication_ID;

-- #10 : Auto jointure(jointure réflexive) : renvoie les playlists avec des noms similaires mais des identifiants différents
SELECT
  p1.Playlist_ID AS Playlist1_ID,
  p1.Nom AS Playlist1_Nom,
  p2.Playlist_ID AS Playlist2_ID,
  p2.Nom AS Playlist2_Nom
FROM
  Playlist p1
JOIN
  Playlist p2 ON p1.Nom = p2.Nom AND p1.Playlist_ID < p2.Playlist_ID;

-- #11 : Sous-requête corrélée : Sélectionne les pseudos des utilisateurs qui ont au moins un follower
SELECT Utilisateur.Pseudo
FROM Utilisateur
WHERE EXISTS (
    SELECT 1
    FROM Follower
    WHERE Follower.Utilisateur_Id = Utilisateur.Utilisateur_ID
);

-- #12 : Sous-requête dans le FROM : compte le nombre de followers pour chaque utilisateur 
SELECT Utilisateur.Pseudo, 
    (SELECT COUNT(*) FROM Follower WHERE Follower.Utilisateur_Id = Utilisateur.Utilisateur_ID) AS NombreFollowers
FROM Utilisateur;

-- #13 : sous-requête dans le Where : renvoie les pseudo des utilisateurs quin ont au moins 1 follower
SELECT Pseudo
FROM Utilisateur
WHERE Utilisateur_ID IN (SELECT Utilisateur_Id FROM Follower);

-- #14 : Agregats nécessitant GROUP BY et HAVING : renvoie le nombre de lieu ayant plus de 5 concerts
SELECT
  L.Lieu_ID,
  L.Nom AS Nom_Lieu,
  COUNT(C.Concert_Id) AS Nombre_Concerts
FROM
  Lieu L
LEFT JOIN
  Concert C ON L.Lieu_ID = C.ID_Lieu
GROUP BY
  L.Lieu_ID, L.Nom
HAVING
  COUNT(C.Concert_Id) > 5;

-- # 15 : Requete impliquant le calcul de deux agrégats : renvoie les utilisateurs qui ont envoyé au moins un message privé
SELECT
  Utilisateur.Utilisateur_ID,
  Utilisateur.Pseudo,
  COUNT(Message_Prive.Message_ID) AS Nombre_Messages,
  ROUND(AVG(LENGTH(Message_Prive.Contenu) - LENGTH(REPLACE(Message_Prive.Contenu, ' ', '')) + 1), 1) AS Moyenne_Mots
FROM
  Utilisateur
LEFT JOIN
  Uti_MP ON Utilisateur.Utilisateur_ID = Uti_MP.Utilisateur_Id
LEFT JOIN
  Message_Prive ON Uti_MP.Message_ID = Message_Prive.Message_ID
GROUP BY
  Utilisateur.Utilisateur_ID, Utilisateur.Pseudo
HAVING
  COUNT(Message_Prive.Message_ID) > 0;

-- #16 : jointure externe (left join) : renvoie le nom de chaque utilisateur ainsi que le nombre de concert auxquels il a participé
SELECT Utilisateur.Pseudo, COUNT(Concert.Concert_Id) AS NombreParticipations
FROM Utilisateur
LEFT JOIN Participe ON Utilisateur.Utilisateur_ID = Participe.Personne_ID
LEFT JOIN Concert ON Participe.Concert_ID = Concert.Concert_Id
GROUP BY Utilisateur.Pseudo;

-- #17 : deux requêtes équivalentes exprimant une condition de totalité  : identifie les utilisateurs qui ont à la fois des followers et des amis 
-- #sans aggregation 
SELECT Pseudo
FROM Utilisateur
WHERE EXISTS (
    SELECT 1
    FROM Follower F
    WHERE F.Utilisateur_Id = Utilisateur.Utilisateur_ID
) AND EXISTS (
    SELECT 1
    FROM Amis A
    WHERE A.Utilisateur_Id = Utilisateur.Utilisateur_ID
);

-- #avec agregation 
SELECT Utilisateur.Utilisateur_ID, Utilisateur.Pseudo
FROM Utilisateur
LEFT JOIN (
  SELECT Utilisateur_Id, COUNT(*) AS FollowerCount
  FROM Follower
  GROUP BY Utilisateur_Id
) AS FollowerCounts ON Utilisateur.Utilisateur_ID = FollowerCounts.Utilisateur_Id
LEFT JOIN (
  SELECT Utilisateur_Id, COUNT(*) AS AmisCount
  FROM Amis
  GROUP BY Utilisateur_Id
) AS AmisCounts ON Utilisateur.Utilisateur_ID = AmisCounts.Utilisateur_Id
WHERE COALESCE(FollowerCounts.FollowerCount, 0) = 0 OR COALESCE(AmisCounts.AmisCount, 0) = 0;

-- #18 : requete avec différences si présence de null : affiche les infoos sur les utilisateurs et leur historique 
-- Requête initiale
SELECT Utilisateur.Pseudo, Historique.Type
FROM Utilisateur
LEFT JOIN Historique ON Utilisateur.Historique_Id = Historique.Historique_ID;

-- #requete sans différence en présence de null
-- Modification pour rendre les résultats équivalents en cas de nulls
SELECT Utilisateur.Pseudo, COALESCE(Historique.Type, '0') AS Type
FROM Utilisateur
LEFT JOIN Historique ON Utilisateur.Historique_Id = Historique.Historique_ID;

-- #19 : requete récursive : calculer le prochain jour off (2023)
WITH ClassementConcerts AS (
  SELECT
    C.Concert_Id,
    C.Nom AS Nom_Concert,
    A.Nom AS Nom_Artiste,
    COUNT(P.Personne_ID) AS Nombre_Participants,
    RANK() OVER (PARTITION BY EXTRACT(MONTH FROM C.Date) ORDER BY COUNT(P.Personne_ID) DESC) AS Classement_Mensuel
  FROM Concert C
  JOIN Participe P ON C.Concert_Id = P.Concert_ID
  JOIN Artistes A ON C.Nom = A.Nom  

  WHERE EXTRACT(YEAR FROM C.Date) = 2023
  GROUP BY C.Concert_Id, C.Nom, A.Nom, C.Date  

)
SELECT
  Concert_Id,
  Nom_Concert,
  Nom_Artiste,
  Nombre_Participants
FROM ClassementConcerts
WHERE Classement_Mensuel <= 10;

-- #20 : requete utilisant du fenetrage : détails des concerts ayant eu lieu en 2023, les classe mensuellement par le nombre de participants et retourne ceux se classant parmi les 10 premiers dans leur mois respectif.
WITH ClassementConcerts AS (
  SELECT
    C.Concert_Id,
    C.Nom AS Nom_Concert,
    A.Nom AS Nom_Artiste,
    COUNT(P.Personne_ID) AS Nombre_Participants,
    RANK() OVER (PARTITION BY EXTRACT(MONTH FROM C.Date) ORDER BY COUNT(P.Personne_ID) DESC) AS Classement_Mensuel
  FROM Concert C
  JOIN Participe P ON C.Concert_Id = P.Concert_ID
  JOIN Artistes A ON C.ID_Lieu = A.Artistes_ID  
  WHERE EXTRACT(YEAR FROM C.Date) = 2023 -- peut etre changé 
  GROUP BY C.Concert_Id, C.Nom, A.Nom  
)
SELECT
  Concert_Id,
  Nom_Concert,
  Nom_Artiste,
  Nombre_Participants
FROM ClassementConcerts
WHERE Classement_Mensuel <= 10;




 