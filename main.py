#!/usrin/env python3
import copy
from typing import List, Iterable
from tcod.console import Console as Console
from message_log import MessageLog

import tcod

from engine import Engine
import entity_factories
from procgen import generate_dungeon
from components.render_order import RenderOrder
from entity import Entity


def main() -> None:
    screen_width = 80
    screen_height = 60
    
    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "Data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    message_console_height = max(5, 1)  # Ensure message_console_height is not 0
    message_console = tcod.Console(screen_width, message_console_height, order="F")
    message_console.default_bg = (50, 50, 50)

    with tcod.context.new_terminal(
        screen_width,
        screen_height + message_console_height,
        tileset=tileset,
        title="Alexei's Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height + message_console_height, order="F")

        if isinstance(player, Entity) and isinstance(message_console, Console):
            engine = Engine(player=player, message_console=message_console)
        else:
            raise TypeError("Player must be an instance of Entity and message_console must be an instance of Console.")

        engine.game_map = generate_dungeon(
            max_rooms=max_rooms,
            room_min_size=room_min_size,
            room_max_size=room_max_size,
            map_width=map_width,
            map_height=map_height,
            max_monsters_per_room=max_monsters_per_room,
            engine=engine,
        )

        engine.update_fov()
        root_console.clear()
        message_console.clear()

        while True:
            render_gui(root_console, engine.player.fighter.hp, engine.player.fighter.max_hp, 20, engine.message_log)
            engine.render(console=root_console, context=context)
            engine.event_handler.handle_events()
            
from render_functions import render_bar, render_messages

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog) -> None:
    print("render_gui called")
    if isinstance(console, Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int):
        render_bar(console, current_value, maximum_value, total_width)
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, and total_width must be integers.")
    y = console.height - message_console_height - 2
    if isinstance(message_log, MessageLog):
        for message in message_log.messages:
            console.print(console.width - 2, y, str(message), fg=(255, 255, 255), bg=(0, 0, 0), alignment=tcod.RIGHT)
            y -= 1
    else:
        raise TypeError("message_log must be an instance of MessageLog.")

if __name__ == "__main__":
    main()
