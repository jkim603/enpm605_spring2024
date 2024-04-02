import sys
import os.path
path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path)
# Import your functions

from rpg.player import Player  # noqa: E402
from rpg.enemy import Enemy  # noqa: E402
import random  # noqa: E402
# from lecture6.rpg.enemy import Enemy
# from lecture6.rpg.maze import Maze
# from lecture6.rpg.item import Item

if __name__ == "__main__":
    # Create a player
    
    player = Player("Link", 150)
    enemy = Enemy("Ganon")
    game_action = [player.attack, enemy.attack]
    
    while player.health > 0:
        action = random.choice(game_action)
        if action == player.attack:
            action(enemy, 20)
        elif action == enemy.attack:
            action(player, 30)
        else:
            print("Invalid action")
