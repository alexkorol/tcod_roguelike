# Updated import of MainGameEventHandler
from __future__ import annotations

<<<<<<< HEAD
from typing import TYPE_CHECKING, List
=======
from typing import TYPE_CHECKING
from message_log import MessageLog, Message
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9

from tcod.context import Context
from tcod.console import Console as Console
from tcod.map import compute_fov

<<<<<<< HEAD
from input_handlers import EventHandler
from render_functions import render_bar
from message_log import MessageLog 
=======
from main_game_event_handler import MainGameEventHandler
from render_functions import render_bar, render_messages
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap

class Engine:
    game_map: GameMap
    message_log: MessageLog
    message_console: Console

    def __init__(self, player: Optional[Entity] = None, message_console: Console = None, message_log: MessageLog = None):
        self.event_handler: MainGameEventHandler = MainGameEventHandler(self)
        self.player = player
        self.message_log = message_log
        self.message_console = message_console

    def set_player(self, player: Entity):
        self.player = player
<<<<<<< HEAD
        self.messages = []
        self.message_log = MessageLog()
=======
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                entity.ai.perform()
    
    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        print("Rendering started")
        print("Rendering game map")
        self.game_map.render(console)
<<<<<<< HEAD

        render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )

        self.message_log.render(console=console, x=21, y=45, width=40, height=5)

=======
        print("Rendering bar")
        render_bar(console, self.player.fighter.hp, self.player.fighter.max_hp, 20)
        print("Rendering message log")
        self.message_log.render(console=console, x=21, y=45, width=40, height=5)
        print("Presenting context")
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9
        context.present(console)
        print("Clearing console")
        console.clear()
        print("Rendering finished")
        
