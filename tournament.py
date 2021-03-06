#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM matches")
    connection.commit()

def deletePlayers():
    """Remove all the player records from the database."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM players")
    connection.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM players")
    connection.commit()
    playerCount = cursor.fetchone()
    return playerCount[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO players VALUES (%s)", (name,))
    connection.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection = connect()
    cursor2 = connection.cursor()
    cursor2.execute("SELECT id FROM players")
    player_ids = cursor2.fetchall()
    cursor1 = connection.cursor()

    # every player is present in the standings table
    for i in range(len(player_ids)):
        opponent = random.choice(player_ids)    # random opponent
        while opponent == player_ids[i]:
            opponent = random.choice(player_ids)
        cursor1.execute("INSERT INTO matches(player, opponent, result)"
                        "VALUES(%s, %s, 2)",
                        (player_ids[i], opponent))

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM standings ORDER BY wins DESC")
    standings = cursor.fetchall()
    connection.commit()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO matches(player, opponent, result)"
                   "VALUES(%s, %s, 1)",
                   (winner, loser))
    cursor.execute("INSERT INTO matches(player, opponent, result)"
                   "VALUES(%s, %s, 0)",
                   (loser, winner))
    connection.commit()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id, standings.name, wins "
                   "FROM standings ORDER BY wins DESC ")
    pairs = cursor.fetchall()
    pairings = []
    i = 0
    while i < len(pairs):
        id1 = pairs[i][0]
        name1 = pairs[i][1]
        id2 = pairs[i+1][0]
        name2 = pairs[i+1][1]
        pairings.append([id1, name1, id2, name2])
        i += 2

    return pairings
