from __future__ import annotations

from typing import TYPE_CHECKING

from components.fighter import Fighter
from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item

class Consumable(BaseComponent):
    def __init__(self, on_use_function=None):
        self.on_use_function = on_use_function

    def get_action(self, consumer: Actor) -> Action:
        """Try to return the action for this item."""
        raise NotImplementedError()

    def activate(self, action: Action) -> None:
        """Invoke this items ability. This should be overridden by Consumable subclasses."""
        raise NotImplementedError()

    def consume(self) -> None:
        """Remove the consumed item."""
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, Actor):
            inventory.inventory.remove(entity)

class HealingConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount

    def get_action(self, consumer: Actor) -> Action:
        return actions.HealingConsumableAction(consumer, self)

    def activate(self, action: Action) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)
        if amount_recovered > 0:
            raise Impossible("Your health is already full.")
        self.consume()
