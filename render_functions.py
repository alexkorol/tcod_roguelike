import tcod
from tcod.console import Console
from message_log import MessageLog

def render_bar(console: tcod.Console, current_value: int, maximum_value: int, total_width: int) -> None:
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
def render_messages(console: Console, x: int, y: int, message_log: MessageLog, n: int) -> None:
    messages_to_render = message_log.get_last_messages(n)
    message_console = Console(console.width, len(messages_to_render))
    message_console.draw_frame(0, 0, message_console.width, message_console.height)
    for i, message in enumerate(messages_to_render):
        message_console.print(0, i, str(message), fg=message.fg)
    console.blit(message_console, x, y)
