# Removed MainGameEventHandler class and updated import
from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, BumpAction, EscapeAction, WaitAction
from main_game_event_handler import MainGameEventHandler, EventHandler

if TYPE_CHECKING:
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        # Removed import of Engine
        pass
    else:
        Engine = 'Engine'


MOVE_KEYS = {
    # Arrow keys.
    tcod.event.KeySym.UP: (0, -1),
    tcod.event.KeySym.DOWN: (0, 1),
    tcod.event.KeySym.LEFT: (-1, 0),
    tcod.event.KeySym.RIGHT: (1, 0),
    tcod.event.KeySym.HOME: (-1, -1),
    tcod.event.KeySym.END: (-1, 1),
    tcod.event.KeySym.PAGEUP: (1, -1),
    tcod.event.KeySym.PAGEDOWN: (1, 1),
    # Numpad keys.
    tcod.event.KeySym.KP_1: (-1, 1),
    tcod.event.KeySym.KP_2: (0, 1),
    tcod.event.KeySym.KP_3: (1, 1),
    tcod.event.KeySym.KP_4: (-1, 0),
    tcod.event.KeySym.KP_6: (1, 0),
    tcod.event.KeySym.KP_7: (-1, -1),
    tcod.event.KeySym.KP_8: (0, -1),
    tcod.event.KeySym.KP_9: (1, -1),
    # Vi keys
    tcod.event.KeySym.h: (-1, 0),
    tcod.event.KeySym.j: (0, 1),
    tcod.event.KeySym.k: (0, -1),
    tcod.event.KeySym.l: (1, 0),
    tcod.event.KeySym.y: (-1, -1),
    tcod.event.KeySym.u: (1, -1),
    tcod.event.KeySym.b: (-1, 1),
    tcod.event.KeySym.n: (1, 1),
}

WAIT_KEYS = {
    tcod.event.KeySym.PERIOD,
    tcod.event.KeySym.KP_5,
    tcod.event.KeySym.CLEAR,
}


class InventoryEventHandler(EventHandler):
    """Handle inventory input events."""

    def on_show_inventory(self) -> None:
        """Show the inventory menu."""
        raise NotImplementedError()

    def on_drop_inventory(self) -> None:
        """Show the drop item menu."""
        raise NotImplementedError()


class InventoryActivateHandler(InventoryEventHandler):
    """Handle inventory activation events."""

    def on_show_inventory(self) -> None:
        """Show the inventory menu for item activation."""
        self.engine.message_log.add_message("Select an item to use it.", tcod.yellow)



class InventoryDropHandler(InventoryEventHandler):
    """Handle inventory drop events."""

    def on_drop_inventory(self) -> None:
        """Show the inventory menu for item dropping."""
        self.engine.message_log.add_message("Select an item to drop it.", tcod.yellow)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index < len(player.inventory.items):
            item = player.inventory.items[index]

            # Return the action to drop the selected item
            return DropItem(player, item)



    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key in WAIT_KEYS:
            action = WaitAction(player)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction(player)

        # No valid key pressed
        return action
