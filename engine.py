from __future__ import annotations

from typing import TYPE_CHECKING
from message_log import MessageLog, Message

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from input_handlers import EventHandler
from render_functions import render_bar, render_messages

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap

class Engine:
    game_map: GameMap
    message_log: MessageLog
    
    def __init__(self, player: Entity):
        self.event_handler: EventHandler = EventHandler(self)
        self.player = player
        self.message_log = MessageLog(0, 0, 4)

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

    def render(self, console: Console, context: Context, n: int) -> None:
        self.game_map.render(console)
        render_bar(console, self.player.fighter.hp, self.player.fighter.max_hp, 20)
        render_messages(console, 0, console.height - n, self.message_log, n)

        context.present(console)

        console.clear()
        
