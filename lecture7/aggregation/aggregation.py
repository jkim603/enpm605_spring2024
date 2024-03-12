class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


class Player:
    def __init__(self, name):
        self.name = name


# Creating objects and establishing aggregation
team = Team("Sharks")
player = Player("Bob")
team.add_player(player)