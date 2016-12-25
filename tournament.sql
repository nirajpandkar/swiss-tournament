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

create view no_wins as
select players.id, count(matches.opponent)
from players, matches
where players.id = matches.player and (matches.result>0 or matches.result == 2)
group by players.id;

create view no_matches as
(select players.id, count(matches.opponent)
from players, matches
where players.id = matches.player
group by players.id);

create view standings as
select players.id, players.name, no_wins.count as wins, no_matches.count as matches
from players, no_wins, no_matches
where players.id=no_wins.id and no_wins.id=no_matches.id;