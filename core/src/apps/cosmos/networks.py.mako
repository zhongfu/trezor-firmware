# generated from networks.py.mako
# do not edit manually!
from typing import Iterator

from apps.common.paths import HARDENED


def shortcut_by_chain_id(chain_id: int) -> str:
    n = by_chain_id(chain_id)
    return n.shortcut if n is not None else "UNKN"


def by_chain_id(chain_id: int) -> "NetworkInfo" | None:
    for n in _networks_iterator():
        if n.chain_id == chain_id:
            return n
    return None


def by_bech32_prefix(bech32_prefix: str) -> "NetworkInfo" | None:
    for n in _networks_iterator():
        if n.bech32_prefix == bech32_prefix:
            return n
    return None


def by_chain_name(name: str) -> "NetworkInfo" | None:
    for n in _networks_iterator():
        if n.name == name:
            return n
    return None


class NetworkInfo:
    def __init__(
        self, chain_id: int, slip44: int, bech32_prefix: str, key_algos: tuple[str], shortcut: str, name: str
    ) -> None:
        self.chain_id = chain_id
        self.slip44 = slip44
        self.bech32_prefix = bech32_prefix
        self.key_algos = key_algos
        self.shortcut = shortcut
        self.name = name


# fmt: off
def _networks_iterator() -> Iterator[NetworkInfo]:
% for n in supported_on("trezor2", cosmos):
    yield NetworkInfo(
        chain_id="${n.chain_id}",
        slip44=${n.slip44},
        bech32_prefix="${n.bech32_prefix}",
        key_algos=${n.key_algos},
        shortcut="${n.shortcut}",
        name="${n.name}"
    )
% endfor
