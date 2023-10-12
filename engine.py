# Updated import of MainGameEventHandler
from __future__ import annotations

from typing import TYPE_CHECKING
from message_log import MessageLog, Message

from tcod.context import Context
from tcod.console import Console as Console
from tcod.map import compute_fov

from main_game_event_handler import MainGameEventHandler
from render_functions import render_bar, render_messages

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap

class Engine:
    game_map: GameMap
    message_log: MessageLog
    message_console: Console

    def __init__(self, player: Entity, message_console: Console, message_log: MessageLog):
        self.event_handler: MainGameEventHandler = MainGameEventHandler(self)
        self.player = player
        self.message_log = message_log
        self.message_console = message_console

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
        print("Rendering bar")
        render_bar(console, self.player.fighter.hp, self.player.fighter.max_hp, 20)
        print("Rendering message log")
        self.message_log.render(console=console, x=21, y=45, width=40, height=5)
        print("Presenting context")
        context.present(console)
        print("Clearing console")
        console.clear()
        print("Rendering finished")
        
