import tcod
from message_log import MessageLog
from render_functions import render_bar, render_gui

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog) -> None:
    if isinstance(console, tcod.Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int):
        render_bar(console, current_value, maximum_value, total_width)
        render_messages(console, message_log)  # Add this line to render the message log
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, and total_width must be integers.")
