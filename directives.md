C:\Users\16178\Documents\Code\tcod_roguelike>python main.py
C:\Users\16178\Documents\Code\tcod_roguelike\render_functions.py:4: FutureWarning: tcod.Console is deprecated.
Replace 'tcod.Console' with 'tcod.console.Console'
  def render_bar(console: tcod.Console, current_value: int, maximum_value: int, total_width: int) -> None:
C:\Users\16178\Documents\Code\tcod_roguelike\main.py:75: FutureWarning: tcod.Console is deprecated.
Replace 'tcod.Console' with 'tcod.console.Console'
  def render_gui(console: tcod.Console, current_value: int, maximum_value: int, total_width: int, message_log: MessageLog, message_console_height: int) -> None:
C:\Users\16178\Documents\Code\tcod_roguelike\main.py:36: FutureWarning: tcod.Console is deprecated.
Replace 'tcod.Console' with 'tcod.console.Console'
  message_console = tcod.Console(screen_width, message_console_height, order="F")
C:\Users\16178\Documents\Code\tcod_roguelike\main.py:37: FutureWarning: Console defaults have been deprecated.
  message_console.default_bg = (50, 50, 50)
C:\Users\16178\Documents\Code\tcod_roguelike\main.py:46: FutureWarning: tcod.Console is deprecated.
Replace 'tcod.Console' with 'tcod.console.Console'
  root_console = tcod.Console(screen_width, screen_height + message_console_height, order="F")
Traceback (most recent call last):
  File "C:\Users\16178\Documents\Code\tcod_roguelike\main.py", line 90, in <module>
    main()
  File "C:\Users\16178\Documents\Code\tcod_roguelike\main.py", line 50, in main
    engine = Engine(player=player, message_console=message_console, message_log=message_log)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Engine.__init__() got an unexpected keyword argument 'message_log'