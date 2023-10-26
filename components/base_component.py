from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class BaseComponent:
    def __init__(self, entity: Entity):  # Modified to accept an entity
        self.entity = entity  # Set the entity here

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine