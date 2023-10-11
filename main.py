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

    player = copy.deepcopy(entity_factories.player)

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
            engine.render(console=root_console, context=context)
            render_gui(root_console, engine.player.fighter.hp, engine.player.fighter.max_hp, 20, engine.message_log, message_console_height)
            engine.event_handler.handle_events()
            
from render_functions import render_bar, render_messages

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog, message_console_height: int) -> None:
    # No operation
    if isinstance(console, Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int):
        render_bar(console, current_value, maximum_value, total_width)
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, and total_width must be integers.")

if __name__ == "__main__":
    main()
class HistoryViewer:
    def __init__(self, engine):
        self.engine = engine
        self.index = 0

    def handle_events(self):
        key = tcod.console_wait_for_keypress(True)
        if key.vk == tcod.KEY_UP:
            self.index = max(0, self.index - 1)
        elif key.vk == tcod.KEY_DOWN:
            self.index = min(len(self.engine.message_log.messages) - 1, self.index + 1)
        elif key.vk == tcod.KEY_ESCAPE:
            self.engine.event_handler = MainGameEventHandler(self.engine)

    def render(self, console):
        console.clear()
        for i, message in enumerate(self.engine.message_log.messages):
            color = (255, 255, 255) if i == self.index else (200, 200, 200)
            console.print(0, i, message.text, fg=color)
