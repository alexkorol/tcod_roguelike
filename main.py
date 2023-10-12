import tcod

from message_log import MessageLog
from render_functions import render_bar, render_messages

def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog) -> None:
    if isinstance(console, tcod.Console) and isinstance(current_value, int) and isinstance(maximum_value, int) and isinstance(total_width, int) and isinstance(message_log, MessageLog):
        render_bar(console, current_value, maximum_value, total_width)
        render_messages(console, message_log)  # Pass the console and message_log arguments
    else:
        raise TypeError("Console must be an instance of Console, and current_value, maximum_value, total_width, and message_log must be of the correct types.")
