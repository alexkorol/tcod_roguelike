<<<<<<< HEAD
from __future__ import annotations

from typing import TYPE_CHECKING

import color

if TYPE_CHECKING:
    from tcod import Console


def render_bar(
    console: Console, current_value: int, maximum_value: int, total_width: int
) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=0, y=45, width=total_width, height=1, ch=1, bg=color.bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=0, y=45, width=bar_width, height=1, ch=1, bg=color.bar_filled
        )

    console.print(
        x=1, y=45, string=f"HP: {current_value}/{maximum_value}", fg=color.bar_text
    )
=======
import tcod
from tcod.console import Console

from message_log import MessageLog

def render_bar(console: Console, current_value: int, maximum_value: int, total_width: int) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    # Draw the total HP bar in red
    console.draw_rect(1, 1, total_width, 1, 0, bg=(255, 0, 0))

    # Draw the remaining HP bar in green
    if bar_width > 0:
        console.draw_rect(1, 1, bar_width, 1, 0, bg=(0, 255, 0))

    # Print the HP value over the bar
    console.print(
        int(total_width / 2), 1, f"HP: {current_value}/{maximum_value}", fg=(255, 255, 255), alignment=tcod.CENTER
    )

def render_messages(console: Console, message_log: MessageLog) -> None:
    console.clear()
    messages_to_render = message_log.get_last_messages(console.height)
    for i, message in enumerate(messages_to_render):
        console.print(0, i, str(message), fg=message.fg)
    console.blit(console, 0, console.height - console.height, 0, 0, console.width, console.height)
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9
