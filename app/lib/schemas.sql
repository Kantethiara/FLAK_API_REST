 --Connexion à la base de données--
\c apidata;

CREATE TYPE utilisateur_role AS ENUM ('admin', 'user');

-- Création des tables
CREATE TABLE groupe (
    id_groupe  SERIAL PRIMARY KEY,
    nom_groupe VARCHAR(255) NOT NULL
   
);

CREATE TABLE utilisateur (
    id_utilisateur  SERIAL PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    motdpass VARCHAR(255) NOT NULL,
    role utilisateur_role NOT NULL ,
    Dcreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_groupe INT,
  CONSTRAINT id_groupe_fk
        FOREIGN KEY(id_groupe) 
        REFERENCES groupe(id_groupe)

);

CREATE TABLE prompt (
    id_prompt SERIAL PRIMARY KEY,
    titre TEXT NOT NULL,
    contenu VARCHAR NOT NULL,
    statut VARCHAR(50) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL DEFAULT 1000.00,
    datecreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    editDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_utilisateur INT,
    CONSTRAINT id_utilisateur_fk
        FOREIGN KEY(id_utilisateur) 
        REFERENCES utilisateur(id_utilisateur)
);

CREATE TABLE prompt_modifications (
    id_modification SERIAL PRIMARY KEY,
    id_prompt INT REFERENCES prompt(id_prompt),
    titre TEXT,
    contenu VARCHAR,
    statut VARCHAR(50),
    prix DECIMAL(10, 2),
    id_utilisateur INT REFERENCES utilisateur(id_utilisateur),
    datecreation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approved BOOLEAN DEFAULT FALSE,
    CONSTRAINT id_prompt_fk

        FOREIGN KEY(id_prompt) 
        REFERENCES prompt(id_prompt),
    CONSTRAINT id_utilisateur_fk
        FOREIGN KEY(id_utilisateur) 
        REFERENCES utilisateur(id_utilisateur)
);


CREATE TABLE vote (
    id_vote SERIAL PRIMARY KEY,
    voteValue INT NOT NULL,
    id_utilisateur INT NOT NULL,
    id_prompt INT NOT NULL,
        FOREIGN KEY(id_utilisateur) 
        REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,,
        FOREIGN KEY(id_prompt) ON DELETE CASCADE,
        REFERENCES Prompt(id_prompt)
);

CREATE TABLE note (
    id_note INT serial PRIMARY KEY,
    noteValue INT NOT NULL,
    id_utilisateur INT NOT NULL,
    id_prompt INT NOT NULL,
        FOREIGN KEY(id_utilisateur) 
        REFERENCES utilisateur(id_utilisateur),
        FOREIGN KEY(id_prompt) 
        REFERENCES prompt(id_prompt)
);


DROP TABLE groupe CASCADE;
SELECT * FROM utilisateur;
SELECT * FROM prompt_modifications;
DROP TABLE prompt CASCADE;


