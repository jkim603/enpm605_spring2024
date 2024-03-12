import sys
import os.path
folder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(folder)
# Import your functions

from rpg.player import Player  # noqa: E402
from rpg.enemy import Enemy  # noqa: E402
import random  # noqa: E402
# from lecture6.rpg.enemy import Enemy
# from lecture6.rpg.maze import Maze
# from lecture6.rpg.item import Item

if __name__ == "__main__":
    player = Player("Link", 150)
    player.name = "Arthur" 
    print(player.name) # Arthur
    # print(Player.name.__doc__) # The name of the player.
