import sys
import os.path
folder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(folder)
# Import your functions

from rpg.enemy import Enemy  # noqa: E402
from rpg.player import Player  # noqa: E402

if __name__ == "__main__":
    enemy = Enemy()
    print(enemy)
    print(enemy.name)