-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE database tournament;
\c tournament;
DROP VIEW IF EXISTS standings;
DROP VIEW IF EXISTS no_wins;
DROP VIEW IF EXISTS no_matches;

CREATE TABLE players(
    name varchar(50) NOT NULL,
    id serial PRIMARY KEY
);

CREATE TABLE matches(
    match_id serial PRIMARY KEY ,
    player int REFERENCES players(id),
    opponent int REFERENCES players(id),
    result int
);

CREATE VIEW no_wins AS
SELECT players.id, count(matches.opponent) AS count_wins
FROM players, matches
WHERE players.id = matches.player AND matches.result>0
GROUP BY players.id;

CREATE VIEW no_matches AS
(SELECT players.id, count(matches.opponent) AS count_matches
FROM players, matches
WHERE players.id = matches.player
GROUP BY players.id);

CREATE VIEW standings AS
SELECT players.id, players.name, no_wins.count_wins AS wins, no_matches
                                                       .count_matches AS
matches
FROM players, no_wins, no_matches
WHERE players.id=no_wins.id AND no_wins.id=no_matches.id;