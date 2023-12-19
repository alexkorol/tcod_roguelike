from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING

from message_log import Message

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity, Item

class Action:
    def __init__(self, entity: Actor, engine: Engine):
        self.entity = entity
        self.engine = engine

    def perform(self) -> None:
        raise NotImplementedError()

class PickupAction(Action):
    def __init__(self, entity: Actor, item: Item, engine: Engine):
        super().__init__(entity, engine)
        self.item = item

    def perform(self) -> None:
        self.entity.inventory.add_item(self.item)
        self.engine.game_map.entities.remove(self.item)

class DropItem(Action):
    def __init__(self, entity: Actor, item: Item, engine: Engine):
        super().__init__(entity, engine)
        self.item = item

    def perform(self) -> None:
        self.entity.inventory.remove_item(self.item)
        self.item.place(self.entity.x, self.entity.y, self.engine.game_map)
        self.engine.game_map.entities.add(self.item)

class EscapeAction(Action):
    def perform(self) -> None:
        raise SystemExit()

class WaitAction(Action):
    def perform(self) -> None:
        pass

class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int, engine: Engine):
        super().__init__(entity, engine)
        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self) -> Tuple[int, int]:
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    @property
    def target_actor(self) -> Optional[Actor]:
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self) -> None:
        raise NotImplementedError()

class MeleeAction(ActionWithDirection):
    def perform(self) -> None:
        target = self.target_actor
        if not target:
            return
        
        damage = self.entity.fighter.power - target.fighter.defense

        attack_desc = f"{self.entity.name.capitalize()} attacks {target.name}"
        if damage > 0:
            self.engine.message_log.add_message(Message(f"{attack_desc} for {damage} hit points", (255, 255, 255)))
            target.fighter.hp -= damage
        else:
            self.engine.message_log.add_message(Message(f"{attack_desc} but does no damage.", (255, 255, 255)))

class MovementAction(ActionWithDirection):
    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            return
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return

        self.entity.move(self.dx, self.dy)

class BumpAction(ActionWithDirection):
    def perform(self) -> None:
        if self.target_actor:
            if self.target_actor.fighter:
                damage = self.entity.fighter.power - self.target_actor.fighter.defense
                if damage > 0:
                    self.target_actor.fighter.take_damage(damage)
                return
            return MeleeAction(self.entity, self.dx, self.dy, self.engine).perform()

        else:
            return MovementAction(self.entity, self.dx, self.dy, self.engine).perform()

class InventoryAction(Action):
    def __init__(self, entity: Actor, item: Item, engine: Engine):
        super().__init__(entity, engine)
        self.item = item

    def perform(self) -> None:
        try:
            self.item.ability.perform()
        except Exception as e:
            print(f"Error: {e}")
