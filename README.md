# Pylorant

API wrapper for Valorant written in Python.

# Installing
To install the library you can just run the following command:
```
pip install pylorant
```

# Example

```python
import Pylorant

account = Pylorant.Account("naTs", "TATAR", "EU")
print(account.rank)

match_history = account.Get_Match_History()
for match in match_history:
    print(match.map)

stats = account.Get_Stats()
print(stats.headshots)
```
# Documentation

## class Account
Used for general datas about the account:
```python
class Account(name, tag, region)
```
The account class has the following variables:
```
string name: name of the account
string tag: tag of the account
string region: region of the account
dict account_data: a dict full of datas took from the account
int level: account's level
dict cards: dict of the cards in use from the player ("small", "large", "wide", "id")
dict mmr_data: all the mmr data received from the request
int tier: rank in number
string rank: rank in string
dict images: dict with all rank images ("small", "large", "triangle_up", "triangle_down")
```
The account class has the following definitions:
```python
def Get_Match_History(mode = None) #List of mode: escalation, spikerush, deathmatch, competitive, unrated, replication

return a list of class Match()
```
```python
def Get_Stats()

return class Stats()
```

## class Match
Stores all the informations about a specific match and a selected player's stats
```python
class Match(id, name)
```
The match class has the following variables:
```
string map: map of the match
string date: the date the match was played
string mode: mode of the match
int rounds: rounds played during the match
string team: which team the selected player has played for (Blue, Red)
bool won: states if the player has won the game or not
string agent: agent played by the player
int kills: how many kills the player has got
int deaths: how many times the played has died
int assists: how many assists the player has got
dict agent_icon: dict with agent icons' urls ("small", "bust", "full", "killfeed")
int dmgperrnd: average damage done by the player each round
int bodyshots: how many bodyshots has the player hit
int legshots: how many legshots has the player hit
int headshots: how many headshots has the player hit
int totalshots: total of the shots the player has hit
```

## class Stats
Average stats the played recorded in the last few games
```python
class Stats()
```
The stats class has the following variables:
```
int totalshots: average amount of shot the player has hit each game
int bodyshots: average amount of bodyshot the player has hit each game
int headshots: average amount of headshot the player has hit each game
int legshots: average amount of legshot the player has hit each game
int kills: average amount of kills the player has got in the last few games
int deaths: average amount of deaths the player has got in the last few games
int assists: average amount of assits the player has got in the last few games
```
