from typing import Tuple, List
from tcod.console import Console
import textwrap

class Message:
    def __init__(self, text: str, fg: Tuple[int, int, int]):
        self.text = text
        self.fg = fg

    def __str__(self) -> str:
        return self.text

class MessageLog:
    def __init__(self, x: int, width: int, height: int):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def render(self, console: Console, x: int, y: int, width: int, height: int) -> None:
        """
        Render the message log using the provided console, starting at position (x, y).
        """
        self.messages = self.messages[-height:]

        for i, message in enumerate(self.messages):
            console.print(x, y + i, message.text, fg=message.fg)

    def add_message(self, message: Message) -> None:
        # Add a message if there is room or remove the first message
        width = max(1, self.width)  # Ensure width is always > 0
        new_msg_lines = textwrap.wrap(message.text, width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room for the new one
            if len(self.messages) == self.height:
                del self.messages[0]

            # Add the new line as a Message object, with the text and the color
            self.messages.append(Message(line, message.fg))

    def get_last_messages(self, n: int) -> List[Message]:
        return self.messages[-n:]

    def get_last_messages(self, n: int) -> List[Message]:
        return self.messages[-n:]

    def __iter__(self):
        return iter(self.messages)
