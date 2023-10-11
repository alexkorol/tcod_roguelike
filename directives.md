Here is a summary of the key steps to add a console readout box for game messages:

Create a MessageLog class to store messages and a Message class to represent each message.

Create a console specifically for rendering messages (message_console). Set its size and order.

When creating the Engine, pass the message_console to it.

In the Engine's render method, render the main display, then render the message log to the message console using the render_messages function.

Blit the message console to the root console after rendering the main display. Make sure to account for the message console height in the root console height.

Throughout the game logic, instead of printing, add messages to the Engine's message log using message_log.add_message().

Make sure to clear both the root console and message console each frame.

To view past messages, create a HistoryViewer input handler that renders the full message log and allows scrolling through it.

The key is passing the message console to the Engine, rendering messages to it each frame, allocating space on the root console to blit it, and using the message log to record messages. Let me know if you have any other questions!