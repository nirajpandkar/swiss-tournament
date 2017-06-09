-- Table definitions for the tournament project.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
    name VARCHAR(50) NOT NULL,
    id SERIAL PRIMARY KEY
);

CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY ,
    player INT REFERENCES players(id) ON DELETE CASCADE ,
    opponent INT REFERENCES players(id) ON DELETE CASCADE,
    result INT
);

CREATE VIEW no_wins AS
    SELECT players.id,
        SUM(CASE matches.result
        WHEN 1 THEN 1
        ELSE 0
        END) AS count_wins
    FROM players, matches
    WHERE players.id = matches.player AND matches.result>0
    GROUP BY players.id;

CREATE VIEW no_matches AS
    SELECT players.id,
        SUM(CASE matches.result
        WHEN 2 THEN 0
        ELSE 1
        END) AS count_matches
    FROM players, matches
    WHERE players.id = matches.player
    GROUP BY players.id;

CREATE VIEW standings AS
    SELECT players.id, players.name, no_wins.count_wins AS wins,
    no_matches.count_matches AS matches
    FROM players, no_wins, no_matches
    WHERE players.id=no_wins.id AND no_wins.id=no_matches.id;