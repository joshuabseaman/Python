class Player:

    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]

    def __repr__(self):
        return f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}"

# Bonus
    @classmethod
    def get_team(cls,team_list):
        player_objects = []
        for dict in team_list:
            player_objects.append(cls(dict))
        return player_objects


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
print(player_kevin)
player_jason = Player(jason)
print(player_jason)
player_kyrie = Player(kyrie)
print(player_kyrie)


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team = []
for dictionary in players:
    player = Player(dictionary)
    new_team.append(player)
print(new_team)
