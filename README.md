# Swiss Style Tournament

> An application in python using PostGreSQL which effectively conducts Swiss Style Tournament

## Files

* `tournament.py` - Contains definition of the functions necessary to run swiss style tournament
* `tournament_test.py` - Contains the tests suite to evaluate the functions in tournament.py
* `tournament.sql` - Contains the SQL database structure required for the Swiss style tournament

## Installation

### Prerequisites

* Git
    * For Windows - [Link](https://github.com/git-for-windows/git/releases/)
    * For several UNIX flavours - [Link](https://git-scm.com/download/linux)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

### Steps for installation

* Open up terminal
    * For windows - Use the link above to download the Git Bash
    * For Unix users - Any favorite terminal
* Make a directory and change directory 
    * For eg: `mkdir Udacity; cd Udacity`
* For downloading VM configuration - 
    * `git clone http://github.com/udacity/fullstack-nanodegree-vm `
    *OR*
    * [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* Move to the vagrant folder - `cd fullstack-nanodegree-vm/vagrant`
* Delete the existing tournament folder if you don't want to start from scratch - `rm -r tournament/`
* Clone this project inside the vagrant folder - 
    * `git clone http://github.com/nirajpandkar/swiss-tournament tournament`
* Run vagrant
    * Download the Linux operating system - `vagrant up`
    * Log-in to the newly installed Linux VM - `vagrant ssh`
    
## Usage

1. Move to the working folder
    * `cd /vagrant/tournament`
2. Load the database
    * `psql -f tournament.sql`
3. Fire up the python console and import tournament
    * `python`
    * `import tournament`
4. Play around with the [functions](#api)
5. Run the code against the given test suite
    * `python tournament_test.py`
    
## API

### tournament.registerPlayer(name)

> Adds a player to the tournament database.
  
The database assigns a unique serial id number for the player.  (This
should be handled by your SQL database schema, not in your Python code.)

**Args**:
  name: the player's full name (need not be unique).
  
### tournament.countPlayers()

> Returns the number of players currently registered.

### tournament.deletePlayers()

> Remove all the player records from the database.

### tournament.deleteMatches()

> Remove all the match records from the database.

### tournament.playerStandings()

> Returns a list of the players and their win records, sorted by wins.

The first entry in the list should be the player in first place, 
or a player tied for first place if there is currently a tie.

**Returns**:
  A list of tuples, each of which contains (id, name, wins, matches):
    _id_: the player's unique id (assigned by the database)
    _name_: the player's full name (as registered)
    _wins_: the number of matches the player has won
    _matches_: the number of matches the player has played
    
### tournament.reportMatch(winner, loser)

> Records the outcome of a single match between two players.

**Args**:
      _winner_:  the id number of the player who won
      _loser_:  the id number of the player who lost
      
### tournament.swissPairings()

> Returns a list of pairs of players for the next round of a match.

Each player is paired with another
player with an equal or nearly-equal win record, that is, a player 
adjacent to him or her in the standings.
  
**Returns**:
  A list of tuples, each of which contains (id1, name1, id2, name2)
    _id1_: the first player's unique id
    _name1_: the first player's name
    _id2_: the second player's unique id
    _name2_: the second player's name

## Contributing

1. Fork it
2. Run: `git clone http://github.com/nirajpandkar/swiss-tournament tournament`
3. `cd tournament`
4. Create your feature branch - `git checkout -b new-feature`
5. Push your modifications to the same branch - `git push origin new-feature`
6. Submit a pull request and wait for it to get reviewed and accepted
7. Celebrate!! Cheers :)

## License

MIT © [Niraj Pandkar](http://github.com/nirajpandkar)