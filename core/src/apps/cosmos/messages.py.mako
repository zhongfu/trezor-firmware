# generated from networks.py.mako
# do not edit manually!
from typing import Iterator


def by_message_name(message_name: str) -> "MessageInfo" | None:
    for m in _messages_iterator():
        if m.message_name == message_name:
            return m
    return None


def by_type_url(type_url: str) -> "MessageInfo" | None:
    for m in _messages_iterator():
        if m.type_url == type_url:
            return m
    return None


class MessageInfo:
    def __init__(
        self, type_url: str, message_name: str
    ) -> None:
        self.type_url = type_url
        self.message_name = message_name


# fmt: off
def _messages_iterator() -> Iterator[MessageInfo]:
% for type_url, message_name in cosmos_messages.items():
    yield MessageInfo(
        type_url="${type_url}",
        message_name="${message_name}"
    )
% endfor
