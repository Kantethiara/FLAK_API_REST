-- Insertion de données dans la table utilisateur
INSERT INTO groupe (nom_groupe)
VALUES
('Groupe A'),
('Groupe B')

INSERT INTO utilisateur (nom_utilisateur, email, motdpass, role, dcreation, id_groupe)
VALUES 
('John Doe', 'john.doe@example.com', 'password123', 'admin', CURRENT_DATE, 1),
('Jane Smith', 'jane.smith@example.com', 'password456', 'user', CURRENT_DATE, 2),
('Alice Johnson', 'alice.johnson@example.com', 'password789', 'user', CURRENT_DATE, 1);

-- Insertion de données dans la table prompt
INSERT INTO prompt (titre, contenu, statut, prix, datecreation, editdate, id_utilisateur)
VALUES
('Premier Prompt', 'Contenu du premier prompt', 'actif', 100, CURRENT_DATE, CURRENT_DATE, 8),
('Deuxième Prompt', 'Contenu du deuxième prompt', 'inactif', 150, CURRENT_DATE, CURRENT_DATE,7),
('Troisième Prompt', 'Contenu du troisième prompt', 'actif', 200, CURRENT_DATE, CURRENT_DATE, 6);



-- Insertion de données dans la table vote
INSERT INTO vote (votevalue, id_utilisateur, id_prompt)
VALUES
(1, 17, 17),
(0, 18, 17),
(1, 17, 18);

-- Insertion de données dans la table note
INSERT INTO note (notevalue, id_utilisateur, id_prompt)
VALUES
(5, 6, 6),
(3, 7, 6),
(4, 6, 7);

SELECT * FROM utilisateur WHERE id_groupe = 1;
SELECT * FROM groupe;
UPDATE groupe SET nom_groupe = 'Groupe A' WHERE id_groupe=1;
UPDATE groupe SET nom_groupe = 'Groupe B' WHERE id_groupe=2;

SELECT * FROM prompt;
DELETE FROM prompt WHERE id_prompt=1;