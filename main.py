#!/usrin/env python3
import copy
from typing import List, Iterable
from tcod.console import Console
from message_log import MessageLog

import tcod

from engine import Engine
import entity_factories
from procgen import generate_dungeon
from components.render_order import RenderOrder
from entity import Entity
from entity import Inventory


def main() -> None:
    screen_width = 80
    screen_height = 50
    
    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "Data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = entity_factories.player  # Remove parentheses to assign the class itself
    orc = entity_factories.orc  # Remove parentheses to assign the class itself
    troll = entity_factories.troll  # Remove parentheses to assign the class itself

    player.inventory = Inventory(26)  # Giving the player an inventory with a capacity of 26

    message_console_height = 5
    message_console = tcod.console.Console(screen_width, message_console_height, order="F")
    message_console.clear(fg=(255, 255, 255), bg=(50, 50, 50))

    with tcod.context.new_terminal(
        screen_width,
        screen_height + message_console_height,
        tileset=tileset,
        title="Alexei's Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height + message_console_height, order="F")

        message_log = MessageLog(x=0, width=screen_width, height=message_console_height)
        if isinstance(player, Entity) and isinstance(message_console, Console):
            engine = Engine(player=player, message_console=message_console, message_log=message_log)
            player.engine = engine
            orc.engine = engine
            troll.engine = engine
        else:
            raise TypeError("Player must be an instance of Entity and message_console must be an instance of Console.")

        max_items_per_room = 2
        engine.game_map = generate_dungeon(
            max_rooms=max_rooms,
            room_min_size=room_min_size,
            room_max_size=room_max_size,
            map_width=map_width,
            map_height=map_height,
            max_monsters_per_room=max_monsters_per_room,
            max_items_per_room=max_items_per_room,
            engine=engine,
        )

        engine.update_fov()
        root_console.clear()
        message_console.clear()

        while True:
            engine.event_handler.handle_events()
            engine.handle_enemy_turns()
            engine.update_fov()
            engine.render(console=root_console, context=context)
            render_gui(root_console, engine.player.fighter.hp, engine.player.fighter.max_hp, 20, engine.message_log)
            
from render_functions import render_bar

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog) -> None:
    if isinstance(console, Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int):
        render_bar(console, current_value, maximum_value, total_width)
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, and total_width must be integers.")

if __name__ == "__main__":
    main()
