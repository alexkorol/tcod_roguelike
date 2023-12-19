#!/usrin/env python3
import copy
<<<<<<< HEAD
from typing import List
from message_log import MessageLog
=======
from typing import List, Iterable
from tcod.console import Console
from message_log import MessageLog

>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9
import tcod
from engine import Engine
import entity_factories
from procgen import generate_dungeon
from components.render_order import RenderOrder
<<<<<<< HEAD
from typing import List
import tcod

=======
from entity import Entity
from entity import Inventory
from render_functions import render_messages, render_bar 
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9

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
    orc = copy.deepcopy(entity_factories.orc)
    troll = copy.deepcopy(entity_factories.troll)

<<<<<<< HEAD
    engine = Engine(player=player, message_log=MessageLog())

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
            engine.render(console=root_console, context=context)
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
=======
    message_console_height = 5
    message_console = tcod.console.Console(screen_width, message_console_height, order="F")
    message_console.clear(fg=(255, 255, 255), bg=(50, 50, 50))
    message_log = MessageLog(x=0, width=screen_width, height=message_console_height)
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9

    engine = Engine(player=player, 
                message_console=message_console,
                message_log=message_log)

    engine.player = player

    player.inventory = Inventory(26)  # Giving the player an inventory with a capacity of 26

    player.engine = engine
    orc.engine = engine
    troll.engine = engine

    with tcod.context.new_terminal(
        screen_width,
        screen_height + message_console_height,
        tileset=tileset,
        title="Alexei's Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height + message_console_height, order="F")

        engine.game_map = generate_dungeon(
            max_rooms=max_rooms,
            room_min_size=room_min_size,
            room_max_size=room_max_size,
            map_width=map_width,
            map_height=map_height,
            max_monsters_per_room=max_monsters_per_room,
            max_items_per_room = 2,
            engine=engine,
        )

        engine.update_fov()
        root_console.clear()
        message_console.clear()

        while True:
            engine.event_handler.handle_events()
<<<<<<< HEAD

def render_messages(console: tcod.Console, messages: List[str]) -> None:
    y = console.height - 2
    for message in messages:
        console.print(console.width - 2, y, message, fg=(255, 255, 255), bg=(0, 0, 0), alignment=tcod.RIGHT)
=======
            engine.handle_enemy_turns()
            engine.update_fov()
            engine.render(console=root_console, context=context)
            render_gui(root_console, engine.player.fighter.hp, engine.player.fighter.max_hp, 20, engine.message_log)
            
from render_functions import render_bar

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog) -> None:
    if isinstance(console, Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int):
        render_bar(console, current_value, maximum_value, total_width)
        render_messages(console, message_log)
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, and total_width must be integers.")
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9

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
    if isinstance(console, tcod.Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int) and isinstance(message_log, MessageLog):
        render_bar(console, current_value, maximum_value, total_width)
        render_messages(console, message_log)  # Pass the console and message_log arguments
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, total_width, and message_log must be of the correct types.")