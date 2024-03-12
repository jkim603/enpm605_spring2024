"""
This file contains the player class.
"""

import random


class Player:
    def __init__(self, name="Hero", health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return f"{self.name} has {self.health} health."

    def __iter__(self):
        return iter([self.name, self.health])

    def __contains__(self, item):
        return item in (self.name, self.health)

    def __call__(self, amount):
        if amount > 0:
            self.health += amount
            print(f"{self.name} is healed by {amount} health points.")
        else:
            print("Invalid healing amount. Please provide a positive integer.")

    def __gt__(self, other):
        if isinstance(other, Player):
            return self.health > other.health
        else:
            raise TypeError("Unsupported operand types for >")

    def __add__(self, other):
        if isinstance(other, int):
            return Player(self.name, self.health + other)
        elif isinstance(other, Player):
            return Player(f"{self.name+other.name}", self.health + other.health)
        else:
            raise TypeError("Unsupported operand types for +")

    def attack(self, enemy, damage):
        """
        Attack the enemy.

        Args:
            enemy (Enemy): The enemy to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🤴🗡️ {self.name} attacks {enemy.name}!")
        enemy.take_damage(damage)

    def defend(self):
        """
        Defend against an attack.
        """
        print(f"🤴🛡️ {self.name} defends!")

    def take_damage(self, damage):
        """
        Take damage from an attack.

        Use random to determine if the player will defend or take damage.
        50% chance to defend, 50% chance to take damage.


        Args:
            damage (int): The amount of damage to take.
        """
        # create a random number between 0 and 1
        # if the number is greater than 0.5, the player will defend
        # if the number is less than 0.5, the player will take damage
        if random.random() > 0.5:
            self.defend()
        else:
            self.health -= damage
            if self.health <= 0:
                print(f"🤴💀 {self.name} has been defeated!")
            else:
                print(f"🤴💚 {self.name} has {self.health} health left.")


if __name__ == "__main__":
    arthur = Player("Arthur")
    arthur.health = "hello"
    arthur.take_damage(50)
