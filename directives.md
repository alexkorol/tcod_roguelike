C:\Users\16178\Documents\Code\tcod_roguelike>python main.py
Traceback (most recent call last):
  File "C:\Users\16178\Documents\Code\tcod_roguelike\main.py", line 9, in <module>
    from engine import Engine
  File "C:\Users\16178\Documents\Code\tcod_roguelike\engine.py", line 10, in <module>
    from input_handlers import EventHandler
  File "C:\Users\16178\Documents\Code\tcod_roguelike\input_handlers.py", line 8, in <module>
    from engine import EventHandler
ImportError: cannot import name 'EventHandler' from partially initialized module 'engine' (most likely due to a circular import) (C:\Users\16178\Documents\Code\tcod_roguelike\engine.py)

C:\Users\16178\Documents\Code\tcod_roguelike>