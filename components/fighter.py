from components.base_component import BaseComponent
from components.render_order import RenderOrder
from message_log import Message

class Fighter(BaseComponent):
    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))

    def die(self) -> None:
        if self.entity == self.engine.player:
            death_message = "You died!"
        else:
            death_message = f"{self.entity.name} is dead!"

        self.entity.char = "%"
        self.entity.color = (191, 0, 0)
        self.entity.blocks_movement = False
        self.entity.ai = None
        self.entity.name = f"{self.entity.name} Corpse"
        self.entity.render_order = RenderOrder.CORPSE

        self.entity.gamemap.engine.message_log.add_message(Message(death_message, (255, 0, 0)))

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
        if self.hp <= 0:
            self.die()
