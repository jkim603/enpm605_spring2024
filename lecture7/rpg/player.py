"""
This file contains the Player class.
"""

import random
from typing import Any, Union


class Player:
    """
    A class representing a player in the game.

    Attributes:
        name (str): The name of the player.
        health (int): The health of the player.

    """
    def __init__(self, name="Hero", health=100):
        self._name = name
        self._health = health

    @property
    def name(self):
        """
        The name of the player.
        """
        return self._name

    # @property
    # def name(self):
    #     """
    #     The name of the player.
    #     """
    #     raise AttributeError("Cannot read the name of the player.")
    
    @name.setter
    def name(self, name):
        raise AttributeError("Cannot change the name of the player.")

    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str):
    #         self._name = name
    #     else:
    #         raise TypeError("Name must be a string")
        
    @name.deleter
    def name(self):
        del self._name
    
    @property
    def health(self):
        """
        The health of the player.
        """
        return self._health
    
    @health.setter
    def health(self, health):
        if isinstance(health, int):
            self._health = health
        else:
            raise TypeError("Health must be an integer")
        
    @health.deleter
    def health(self):
        del self._health

    # def _get_name(self):
    #     return self._name
    
    # def _get_health(self):
    #     return self._health
    
    # def _del_name(self):
    #     del self._name
    
    # def _set_name(self, name):
    #     if isinstance(name, str):
    #         self._name = name
    #     else:
    #         raise TypeError("Name must be a string")

    # def _set_health(self, health):
    #     if isinstance(health, int):
    #         self._health = health
    #     else:
    #         raise TypeError("Health must be an integer")
    
    # def _del_health(self):
    #     del self._health
    
    # name = property(fget=_get_name, fset=_set_name, fdel=_del_name, doc="The name of the player.")
    # health = property(fget=_get_health, fset=_set_health, fdel=_del_health, doc="The health of the player.")

    def __str__(self):
        """
        Returns the string representation of the player.

        Returns:
            str: The string representation of the player.
        """
        return f"{self.name} has {self.health} health."
    
    def __repr__(self):
        """
        Returns the string representation of the player.
        """

    def __iter__(self):
        """
        Returns an iterator for the player.

        Returns:
            Iterator[str|int]: An iterator for the player.
        """
        return iter([self.name, self.health])

    def __contains__(self, item: Any):
        """
        Returns whether the player contains the item.

        Args:
            item (Any): The item to check for.

        Returns:
            bool: Whether the player contains the item.
        """
        return item in (self.name, self.health)

    def __call__(self, amount: int):
        """
        Heals the player by the given amount.

        Args:
            amount (int): The amount to heal the player by.
        """
        if amount > 0:
            self.health += amount
            print(f"{self.name} is healed by {amount} health points.")
        else:
            print("Invalid healing amount. Please provide a positive integer.")

    def __gt__(self, other: "Player"):
        """
        Returns whether the player has more health than the other player.

        Args:
            other (Player): The other player to compare health with.

        Raises:
            TypeError: If the other object is not a player.

        Returns:
            bool: Whether the player has more health than the other player.
        """
        if isinstance(other, Player):
            return self.health > other.health
        else:
            raise TypeError("Unsupported operand types for >")

    def __add__(self, other: Union[int, "Player"]):
        """
        Adds the player's health to the other player's health or to the given amount.

        Args:
            other (int|"Player"): The other player or the amount to add to the player's health.

        Raises:
            TypeError: If the other object is not a player or an integer.

        Returns:
            Player: The new player with the combined health.
        """
        if isinstance(other, int):
            return Player(self.name, self.health + other)
        elif isinstance(other, Player):
            return Player(f"{self.name+other.name}", self.health + other.health)
        else:
            raise TypeError("Unsupported operand types for +")

    def attack(self, enemy: "Enemy", damage: int):
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


    @classmethod
    def create_players(cls):
        """
        Create a list of players.

        Returns:
            list[Player]: A list of players.
        """
        return [cls("Player 1", 100), cls("Player 2", 100)]
    
    # Create a super player
    @classmethod
    def create_super_player(cls):
        """
        Create a super player.

        Returns:
            Player: A super player.
        """
        return cls("Super Player", 1000)

    @staticmethod
    def is_valid_player_name(name):
        """
        Check if the provided name is a valid player name.

        Args:
            name (str): The name to check.

        Returns:
            bool: True if valid, False otherwise.
        """
        return isinstance(name, str) and len(name) > 3
    
if __name__ == "__main__":
    name = "Joe"
    print(Player.is_valid_player_name(name))  # False
    name = "Jack"
    print(Player.is_valid_player_name(name))  # True

