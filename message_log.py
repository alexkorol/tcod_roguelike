<<<<<<< HEAD
from typing import List, Reversible, Tuple
import textwrap

import tcod

import color


class Message:
    def __init__(self, text: str, fg: Tuple[int, int, int]):
        self.plain_text = text
        self.fg = fg
        self.count = 1

    @property
    def full_text(self) -> str:
        """The full text of this message, including the count if necessary."""
        if self.count > 1:
            return f"{self.plain_text} (x{self.count})"
        return self.plain_text


class MessageLog:
    def __init__(self) -> None:
        self.messages: List[Message] = []

    def add_message(
        self, text: str, fg: Tuple[int, int, int] = color.white, *, stack: bool = True,
    ) -> None:
        """Add a message to this log.
        `text` is the message text, `fg` is the text color.
        If `stack` is True then the message can stack with a previous message
        of the same text.
        """
        if stack and self.messages and text == self.messages[-1].plain_text:
            self.messages[-1].count += 1
        else:
            self.messages.append(Message(text, fg))

    def render(
        self, console: tcod.Console, x: int, y: int, width: int, height: int,
    ) -> None:
        """Render this log over the given area.
        `x`, `y`, `width`, `height` is the rectangular region to render onto
        the `console`.
        """
        self.render_messages(console, x, y, width, height, self.messages)

    @staticmethod
    def render_messages(
        console: tcod.Console,
        x: int,
        y: int,
        width: int,
        height: int,
        messages: Reversible[Message],
    ) -> None:
        """Render the messages provided.
        The `messages` are rendered starting at the last message and working
        backwards.
        """
        y_offset = height - 1

        for message in reversed(messages):
            for line in reversed(textwrap.wrap(message.full_text, width)):
                console.print(x=x, y=y + y_offset, string=line, fg=message.fg)
                y_offset -= 1
                if y_offset < 0:
                    return  # No more space to print messages.
=======
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
>>>>>>> a13183d596d1e33f8e7c537c8535ea251fdbdbf9
