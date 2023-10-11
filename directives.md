 It looks like the main issue is that the message console is not being blitted to the root console correctly. Here are a few things to try:

1. In render_messages(), make sure to specify the y position when blitting:

```python
console.blit(message_console, 0, console.height - message_console.height)
```

2. In main.py, make sure the root console height accounts for the message console height:  

```python
root_console = tcod.Console(screen_width, screen_height + message_console_height)
```

3. In main.py render_gui(), subtract the message console height when printing the messages:

```python 
y = console.height - message_console_height - 2
```

4. Make sure the message console height is not 0.

5. Call engine.render() before render_gui() so the main console is drawn first.

6. Try setting the message console background color to distinguish it:

```python
message_console = tcod.Console(screen_width, message_console_height, order="F", bg=(50, 50, 50))
```

Let me know if any of those help or if you're still seeing issues!