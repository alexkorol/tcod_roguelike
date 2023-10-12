from __future__ import annotations

import copy
from typing import Optional, Tuple, Type, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from components.ai import BaseAI
    from components.fighter import Fighter
    from components.consumable import Consumable
    from game_map import GameMap
    

T = TypeVar("T", bound="Entity")


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    gamemap: GameMap
    engine: Engine

    def __init__(
        self,
        gamemap: Optional[GameMap] = None,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
        engine: Optional[Engine] = None,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            # If gamemap isn't provided now then it will be set later.
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location. Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if gamemap:
                if hasattr(self, "gamemap"):  # Possibly uninitialized.
                    self.gamemap.entities.remove(self)
                self.gamemap = gamemap
                gamemap.entities.add(self)

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    
# Removed unnecessary import

class Actor(Entity):
    def __init__(
        self,
        *,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        ai_cls: Type[BaseAI],
        fighter: Fighter,
        inventory: Inventory,
        render_order: RenderOrder,
        engine: Engine
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=True,
            engine=engine
        )

        self.ai: Optional[BaseAI] = ai_cls(self, engine)
        self.fighter = fighter
        self.fighter.entity = self
        self.inventory = inventory
        self.inventory.entity = self
        self.render_order = render_order
        
    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)
class Item(Entity):
    """
    A generic object to represent items.
    """

    def __init__(
        self,
        *,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        consumable: Consumable,
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=False,
        )

        self.consumable = consumable
        self.consumable.entity = self

    def spawn(self, gamemap: GameMap, x: int, y: int) -> "Item":
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

class Consumable:
    def consume(self):
        # Implement consume logic here
        pass

class HealingConsumable(Consumable):
    def __init__(self, healing_amount: int):
        super().__init__()
        self.healing_amount = healing_amount

    def activate(self):
        # Implement activation logic here
        pass

    def get_action(self):
        # Implement get_action logic here
        pass

class Inventory:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) >= self.capacity:
            raise Exception("Inventory is full.")
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
