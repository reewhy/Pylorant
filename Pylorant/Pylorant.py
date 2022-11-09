import requests
import json

class Account():
    def __init__(self, name, tag, region):
        self.name = name
        self.tag = tag
        self.region = region

        self.account_data = requests.get(url=f'https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}').json()
        self.region = self.account_data['data']['region']
        self.level = self.account_data["data"]["account_level"]
        self.cards = self.account_data["data"]['card']

    def Get_MMR(self):
        self.mmr_data = requests.get(url=f"https://api.henrikdev.xyz/valorant/v1/mmr/{self.region}/{self.name}/{self.tag}").json()
        self.tier = self.mmr_data['data']['currenttier']
        self.rank = self.mmr_data['data']['currenttierpatched']
        self.images = self.mmr_data['data']['images']

    def Get_Match_History(self, mode = None):
        matches = []
        if mode == None:
            matchhistory = requests.get(url=f'https://api.henrikdev.xyz/valorant/v3/matches/{self.region}/{self.name}/{self.tag}').json()
        else:
            matchhistory = requests.get(url=f'https://api.henrikdev.xyz/valorant/v3/matches/{self.region}/{self.name}/{self.tag}?filter={mode}').json()
        for match in matchhistory['data']:
            matches.append(Match(match['metadata']['matchid'], self.name))
        return matches

    def Get_Stats(self):
        return Stats(self.name, self.tag, self.region)

class Match():
    def __init__(self, id, name):
        global user_player

        data = requests.get(url=f'https://api.henrikdev.xyz/valorant/v2/match/{id}').json()['data']

        for player in data['players']['all_players']:
            if name.lower() == player['name'].lower():
                user_player = player

        self.map = data['metadata']['map']
        self.date = data['metadata']['game_start_patched']
        self.mode = data['metadata']['mode']
        self.rounds = data['metadata']['rounds_played']
        self.team = user_player['team'].lower()
        self.won = data['teams'][self.team]['has_won']
        self.agent = user_player['character']
        self.kills = user_player['stats']['kills']
        self.death = user_player['stats']['deaths']
        self.assists = user_player['stats']['assists']
        self.agenticonurl = user_player['assets']['agent']['small']
        self.dmgperrnd = user_player['damage_made'] / self.rounds
        self.bodyshots = user_player['stats']['bodyshots']
        self.headshots = user_player['stats']['headshots']
        self.legshots = user_player['stats']['legshots']
        self.totalshots = self.bodyshots + self.headshots + self.legshots

class Stats():
    kills = 0
    deaths = 0
    assists = 0
    rounds = 0
    bodyshots = 0
    headshots = 0
    legshots = 0
    def __init__(self, name, tag, region):
        global user_player

        player = Account(name, tag, region)
        matches = player.Get_Match_History(mode='competitive')
        for match in matches:
            self.kills += match.kills
            self.deaths += match.death
            self.assists += match.assists
            self.rounds += match.rounds
            self.bodyshots += match.bodyshots
            self.headshots += match.headshots
            self.legshots += match.legshots

        self.totalshots = round((self.bodyshots + self.legshots + self.headshots) / len(matches), 1)
        self.bodyshots = round(self.bodyshots / len(matches), 1)
        self.headshots = round(self.headshots / len(matches), 1)
        self.legshots = round(self.legshots / len(matches), 1)
        self.kills = round(self.kills / len(matches), 1)
        self.deaths = round(self.deaths / len(matches), 1)
        self.assists = round(self.assists / len(matches), 1)
