import tcod

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
