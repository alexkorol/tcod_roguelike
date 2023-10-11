from typing import Tuple, List
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

    def add_message(self, message: Message) -> None:
        # Add a message if there is room or remove the first message
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room for the new one
            if len(self.messages) == self.height:
                del self.messages[0]

            # Add the new line as a Message object, with the text and the color
            self.messages.append(Message(line, message.fg))

    def get_messages(self) -> List[Message]:
        return self.messages
