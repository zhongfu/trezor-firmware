from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..crypto import Scalar


class CtKey:
    __slots__ = ("dest", "mask")

    def __init__(self, dest: Scalar, mask: Scalar) -> None:
        self.dest = dest
        self.mask = mask
