 There are a few key differences between the tutorial code and yours:

1. The tutorial creates the message log and passes it to the Engine on initialization:

```python
engine = Engine(player=player)
engine.message_log = MessageLog()
```

In your code, you are not passing the message log to the Engine.

2. The tutorial renders the message log in the Engine's render method:

```python
self.message_log.render(console=console, x=21, y=45, width=40, height=5)
``` 

Your render function is not rendering the message log.

3. The tutorial accounts for the message log height in the root console height:

```python
screen_height = 50 
```

Your root console height does not account for the message console height.

4. The tutorial calls engine.render() before rendering the GUI/HUD elements. Your code calls render_gui() first.

So in summary, the key fixes:

- Pass the message log to the Engine on initialization 
- Render the message log in the Engine's render method
- Adjust the root console height for the message console
- Call engine.render() before rendering GUI elements

This should get the message log rendering correctly! Let me know if you have any other questions.