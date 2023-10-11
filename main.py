#!/usrin/env python3
import copy
from typing import List
from tcod.console import Console as Console
from message_log import MessageLog

import tcod

from engine import Engine
import entity_factories
from procgen import generate_dungeon
from components.render_order import RenderOrder


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

    message_console_height = 5
    message_console = tcod.Console(screen_width, message_console_height, order="F")

    with tcod.context.new_terminal(
        screen_width,
        screen_height + message_console_height,
        tileset=tileset,
        title="Alexei's Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")

    engine = Engine(player=player, message_console=message_console)

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
            engine.render(console=root_console, context=context, n=4)
            render_gui(root_console, engine.player.fighter.hp, engine.player.fighter.max_hp, 20, engine.message_log)
            engine.event_handler.handle_events()
            
from render_functions import render_bar, render_messages

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, messages: List[str]) -> None:
    print("render_gui called")
    render_bar(console, current_value, maximum_value, total_width)
    y = console.height - 2
    for message in messages:
        console.print(console.width - 2, y, message, fg=(255, 255, 255), bg=(0, 0, 0), alignment=tcod.RIGHT)
        y -= 1

if __name__ == "__main__":
    main()
