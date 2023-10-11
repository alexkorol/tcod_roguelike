from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor
from components.inventory import Inventory
from components.render_order import RenderOrder

# Define health_potion here
# Replace None with the actual definition of health_potion
# For example, if health_potion is an instance of a class Item, it might look something like this:
# health_potion = Item(...)

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(26),
    render_order=RenderOrder.ACTOR,
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(0),
    render_order=RenderOrder.ACTOR,
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(0),
    render_order=RenderOrder.ACTOR,
)
