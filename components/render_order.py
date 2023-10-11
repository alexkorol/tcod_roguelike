from enum import auto, Enum

class RenderOrder(Enum):
    ACTOR = auto()
    CORPSE = auto()
    ITEM = auto()