#!/usrin/env python3
import copy
from typing import List

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

    engine = Engine(player=player)

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

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Alexei's Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            Engine.render(console=root_console, context=context)
            render_messages(root_console, engine.messages)
            engine.event_handler.handle_events()
            
def render_bar(console: tcod.Console, current_value: int, maximum_value: int, total_width: int) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(1, 1, total_width, 1, 0, bg=(255, 0, 0))
    if bar_width > 0:
        console.draw_rect(1, 1, bar_width, 1, 0, bg=(0, 255, 0))

    console.print(
        int(total_width / 2), 1, f"HP: {current_value}/{maximum_value}", fg=(255, 255, 255), alignment=tcod.CENTER
    )

def render_gui(console: tcod.Console, messages: List[str]) -> None:
    y = console.height - 2
    for message in messages:
        console.print(console.width - 2, y, message, fg=(255, 255, 255), bg=(0, 0, 0), alignment=tcod.RIGHT)
        y -= 1

def main() -> None:
    # ... existing code ...

    while True:
        engine.render(console=root_console, context=context)
        render_gui(root_console, engine.messages)
        engine.event_handler.handle_events()

if __name__ == "__main__":
    main()
