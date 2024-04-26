-- PARTIE 3) Requetes 

-- #1 : Lister tous les concerts avec leurs détails
SELECT C.*, L.Nom AS Lieu_Nom, L.Adresse AS Lieu_Adresse
FROM Concert C
JOIN Lieu L ON C.ID_Lieu = L.Lieu_ID;

-- #2 : Afficher les utilisateurs et leurs playlists associées 
SELECT U.Pseudo, P.Nom AS Playlist_Nom
FROM Utilisateur U
LEFT JOIN Playlist P ON U.Playlist_Id = P.Playlist_ID;

-- #3 : Afficher les utilisateurs et leurs annonces de concerts associées
SELECT C.Nom AS Concert_Nom, L.Nom AS Lieu_Nom
FROM Concert C
INNER JOIN Lieu L ON C.ID_Lieu = L.Lieu_ID;

-- #4 : Récupérer les morceaux d'une playlist spécifique
SELECT M.*
FROM Morceau M
JOIN PlaylistMorceau PM ON M.Morceau_Id = PM.Morceau_Id
WHERE PM.Playlist_Id = 4 ;

-- #5: Obtenir les lieux associés à un tag spécifique 
SELECT L.*
FROM Lieu L
JOIN Tag_Lieu TL ON L.Lieu_ID = TL.Lieu_ID
WHERE TL.Tag_Id = 8;

-- #6 : Renvoyer les 5 concerts ayant le plus de participants
SELECT C.Concert_Id, C.Nom AS Nom_Concert, COUNT(P.Personne_ID) AS Nombre_Participants
FROM Concert C
JOIN Participe P ON C.Concert_Id = P.Concert_ID
GROUP BY C.Concert_Id, C.Nom
ORDER BY Nombre_Participants DESC
LIMIT 5;

-- #7 : Afficher les morceaux et les playlists auxquelles ils appartiennent
SELECT M.Titre, P.Nom AS Playlist_Nom
FROM Morceau M
LEFT JOIN PlaylistMorceau PM ON M.Morceau_Id = PM.Morceau_Id
LEFT JOIN Playlist P ON PM.Playlist_Id = P.Playlist_Id;

-- #8 : Utilisateurs qui ont créé des playlists de groupe
SELECT U.Utilisateur_ID, U.Pseudo, P.Playlist_ID, P.Nom AS Nom_Playlist
FROM Utilisateur U
JOIN Playlist P ON U.Playlist_Id = P.Playlist_ID
WHERE P.IsGroupe;

-- #9 : Requetes sur au moins 3 tables : Renvoie une liste d'utilisateurs avec des infos sur leur historique/publications
SELECT U.Pseudo, H.Type, P.Date AS Publication_Date
FROM Utilisateur U
JOIN Historique H ON U.Historique_Id = H.Historique_ID
LEFT JOIN Publication P ON U.Publication_Id = P.Publication_ID;

-- #10 : Auto jointure(jointure réflexive) : Renvoie les playlists avec des noms similaires mais des identifiants différents
SELECT
  P1.Playlist_ID AS Playlist1_ID,
  P1.Nom AS Playlist1_Nom,
  P2.Playlist_ID AS Playlist2_ID,
  P2.Nom AS Playlist2_Nom
FROM
  Playlist P1
JOIN
  Playlist P2 ON P1.Nom = P2.Nom AND P1.Playlist_ID < P2.Playlist_ID;

-- #11 : Sous-requête corrélée : Sélectionne les pseudos des utilisateurs qui ont au moins un follower
SELECT U.Pseudo
FROM Utilisateur U
WHERE EXISTS (
    SELECT 1
    FROM Follower F
    WHERE F.Utilisateur_Id = U.Utilisateur_ID
);

-- #12 : Sous-requête dans le FROM : Compter le nombre de followers pour chaque utilisateur 
SELECT U.Pseudo, 
    (SELECT COUNT(*) FROM Follower F WHERE F.Utilisateur_Id = U.Utilisateur_ID) AS NombreFollowers
FROM Utilisateur U;

-- #13 : Sous-requête dans le WHERE : Renvoie les pseudos des utilisateurs qui ont au moins 1 follower
SELECT U.Pseudo
FROM Utilisateur U
WHERE U.Utilisateur_ID IN (SELECT F.Utilisateur_Id FROM Follower F);

-- #14 : Agrégats nécessitant GROUP BY et HAVING : Renvoie le nombre de lieux ayant plus de 5 concerts
SELECT L.Lieu_ID, L.Nom AS Nom_Lieu, COUNT(C.Concert_Id) AS Nombre_Concerts
FROM Lieu L
LEFT JOIN Concert C ON L.Lieu_ID = C.ID_Lieu
GROUP BY L.Lieu_ID, L.Nom
HAVING COUNT(C.Concert_Id) > 5;

-- # 15 : Requête impliquant le calcul de deux agrégats : Renvoie les utilisateurs qui ont envoyé au moins un message privé
SELECT U.Utilisateur_ID, U.Pseudo, COUNT(MP.Message_ID) AS Nombre_Messages,
  ROUND(AVG(LENGTH(MP.Contenu) - LENGTH(REPLACE(MP.Contenu, ' ', '')) + 1), 1) AS Moyenne_Mots
FROM Utilisateur U
LEFT JOIN Uti_MP UMP ON U.Utilisateur_ID = UMP.Utilisateur_Id
LEFT JOIN Message_Prive MP ON UMP.Message_ID = MP.Message_ID
GROUP BY U.Utilisateur_ID, U.Pseudo
HAVING COUNT(MP.Message_ID) > 0;

-- #16 : Jointure externe (left join) : Renvoie le nom de chaque utilisateur ainsi que le nombre de concerts auxquels il a participé
SELECT U.Pseudo, COUNT(C.Concert_Id) AS NombreParticipations
FROM Utilisateur U
LEFT JOIN Participe P ON U.Utilisateur_ID = P.Personne_ID
LEFT JOIN Concert C ON P.Concert_ID = C.Concert_Id
GROUP BY U.Pseudo;

-- #17 : Deux requêtes équivalentes exprimant une condition de totalité : Identifie les utilisateurs qui ont à la fois des followers et des amis 
-- #sans agrégation 
SELECT U.Pseudo
FROM Utilisateur U
WHERE EXISTS (
    SELECT 1
    FROM Follower F
    WHERE F.Utilisateur_Id = U.Utilisateur_ID
) AND EXISTS (
    SELECT 1
    FROM Amis A
    WHERE A.Utilisateur_Id = U.Utilisateur_ID
);

-- #avec agrégation 
SELECT U.Utilisateur_ID, U.Pseudo
FROM Utilisateur U
LEFT JOIN (
  SELECT Utilisateur_Id, COUNT(*) AS FollowerCount
  FROM Follower
  GROUP BY Utilisateur_Id
) AS FC ON U.Utilisateur_ID = FC.Utilisateur_Id
LEFT JOIN (
  SELECT Utilisateur_Id, COUNT(*) AS AmisCount
  FROM Amis
  GROUP BY Utilisateur_Id
) AS AC ON U.Utilisateur_ID = AC.Utilisateur_Id
WHERE COALESCE(FC.FollowerCount, 0) = 0 OR COALESCE(AC.AmisCount, 0) = 0;

-- #18 : Requête avec différences si présence de null : Affiche les informations sur les utilisateurs et leur historique 
-- Requête initiale
SELECT U.Pseudo, H.Type
FROM Utilisateur U
LEFT JOIN Historique H ON U.Historique_Id = H.Historique_ID;

-- # Requête modifiée pour rendre les résultats équivalents en cas de nulls
SELECT U.Pseudo, COALESCE(H.Type, '0') AS Type
FROM Utilisateur U
LEFT JOIN Historique H ON U.Historique_Id = H.Historique_ID;

-- #19 : Requête récursive : Calculer le prochain jour off (2023)
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

-- #20 : Requête utilisant du fenêtrage : Détails des concerts ayant eu lieu en 2023, les classe mensuellement par le nombre de participants et retourne ceux se classant parmi les 10 premiers dans leur mois respectif.
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
  WHERE EXTRACT(YEAR FROM C.Date) = 2023 -- peut être modifié 
  GROUP BY C.Concert_Id, C.Nom, A.Nom  
)
SELECT
  Concert_Id,
  Nom_Concert,
  Nom_Artiste,
  Nombre_Participants
FROM ClassementConcerts
WHERE Classement_Mensuel <= 10;
