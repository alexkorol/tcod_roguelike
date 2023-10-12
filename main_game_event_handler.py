from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import tcod.event
from actions import Action, BumpAction, EscapeAction, WaitAction
# Ensure to import InventoryAction if it's defined in the actions module
from actions import InventoryAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler:
    def handle_events(self):
        raise NotImplementedError()

class MainGameEventHandler(EventHandler):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self):
        # TODO: Implement the logic for handling events in this subclass.
        pass

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        key = event.sym
        player = self.engine.player

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key in WAIT_KEYS:
            action = WaitAction(player)
        elif key == tcod.event.K_i:
            # Inventory actions
            action = InventoryAction(player)

        # No valid key pressed
        return action

    
