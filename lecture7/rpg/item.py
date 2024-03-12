from dataclasses import dataclass
from enum import Enum, auto


class ItemType(Enum):
    """
    Enum class for item types
    
    Attributes:
    HEART - heart item
    KEY - key item
    ARROW - arrow item
    """
    HEART = auto()
    KEY = auto()
    ARROW = auto()


@dataclass(frozen=True)
class Item:
    """
    Data class for items in the game
    
    Attributes:
    name: str - name of the item
    item_type: ItemType - type of the item
    """
    name: str
    item_type: ItemType

if __name__ == "__main__":
    # Examples of creating items
    heart_item = Item("Heart", ItemType.HEART)
    key_item = Item("Key", ItemType.KEY)
    arrow_item = Item("Arrow", ItemType.ARROW)

    print(heart_item)
    print(key_item)
    print(arrow_item)