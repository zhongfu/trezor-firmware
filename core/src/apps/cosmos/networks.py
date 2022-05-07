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
    yield NetworkInfo(
        chain_id="agoric-3",
        slip44=564,
        bech32_prefix="agoric",
        key_algos=('secp256k1',),
        shortcut="BLD",
        name="Agoric"
    )
    yield NetworkInfo(
        chain_id="akashnet-2",
        slip44=118,
        bech32_prefix="akash",
        key_algos=('secp256k1',),
        shortcut="AKT",
        name="Akash"
    )
    yield NetworkInfo(
        chain_id="arkh",
        slip44=118,
        bech32_prefix="arkh",
        key_algos=('secp256k1',),
        shortcut="ARKH",
        name="Arkhadian"
    )
    yield NetworkInfo(
        chain_id="mantle-1",
        slip44=118,
        bech32_prefix="mantle",
        key_algos=('secp256k1',),
        shortcut="MNTL",
        name="Asset Mantle"
    )
    yield NetworkInfo(
        chain_id="axelar-dojo-1",
        slip44=118,
        bech32_prefix="axelar",
        key_algos=('secp256k1',),
        shortcut="AXL",
        name="Axelar"
    )
    yield NetworkInfo(
        chain_id="laozi-mainnet",
        slip44=494,
        bech32_prefix="band",
        key_algos=('secp256k1',),
        shortcut="BAND",
        name="BandChain"
    )
    yield NetworkInfo(
        chain_id="bitcanna-1",
        slip44=118,
        bech32_prefix="bcna",
        key_algos=('secp256k1',),
        shortcut="BCNA",
        name="BitCanna"
    )
    yield NetworkInfo(
        chain_id="bitsong-2b",
        slip44=639,
        bech32_prefix="bitsong",
        key_algos=('secp256k1',),
        shortcut="BTSG",
        name="BitSong"
    )
    yield NetworkInfo(
        chain_id="bostrom",
        slip44=118,
        bech32_prefix="bostrom",
        key_algos=('secp256k1',),
        shortcut="BOOT",
        name="bostrom"
    )
    yield NetworkInfo(
        chain_id="carbon-1",
        slip44=118,
        bech32_prefix="swth",
        key_algos=('secp256k1',),
        shortcut="SWTH",
        name="Carbon"
    )
    yield NetworkInfo(
        chain_id="cerberus-chain-1",
        slip44=118,
        bech32_prefix="cerberus",
        key_algos=('secp256k1',),
        shortcut="CRBRUS",
        name="Cerberus"
    )
    yield NetworkInfo(
        chain_id="cheqd-mainnet-1",
        slip44=118,
        bech32_prefix="cheqd",
        key_algos=('secp256k1',),
        shortcut="CHEQ",
        name="cheqd"
    )
    yield NetworkInfo(
        chain_id="chihuahua-1",
        slip44=118,
        bech32_prefix="chihuahua",
        key_algos=('secp256k1',),
        shortcut="HUAHUA",
        name="Chihuahua"
    )
    yield NetworkInfo(
        chain_id="comdex-1",
        slip44=118,
        bech32_prefix="comdex",
        key_algos=('secp256k1',),
        shortcut="CMDX",
        name="Comdex"
    )
    yield NetworkInfo(
        chain_id="cosmoshub-4",
        slip44=118,
        bech32_prefix="cosmos",
        key_algos=('secp256k1',),
        shortcut="ATOM",
        name="Cosmos Hub"
    )
    yield NetworkInfo(
        chain_id="crescent-1",
        slip44=118,
        bech32_prefix="cre",
        key_algos=('secp256k1',),
        shortcut="CRE",
        name="Crescent"
    )
    yield NetworkInfo(
        chain_id="cronosmainnet_25-1",
        slip44=60,
        bech32_prefix="crc",
        key_algos=('secp256k1',),
        shortcut="CRO",
        name="Cronos"
    )
    yield NetworkInfo(
        chain_id="crypto-org-chain-mainnet-1",
        slip44=394,
        bech32_prefix="cro",
        key_algos=('secp256k1',),
        shortcut="CRO",
        name="Crypto.org"
    )
    yield NetworkInfo(
        chain_id="darchub",
        slip44=118,
        bech32_prefix="darc",
        key_algos=('secp256k1',),
        shortcut="DARC",
        name="Konstellation Network"
    )
    yield NetworkInfo(
        chain_id="mainnet-3",
        slip44=118,
        bech32_prefix="decentr",
        key_algos=('secp256k1',),
        shortcut="DEC",
        name="Decentr"
    )
    yield NetworkInfo(
        chain_id="desmos-mainnet",
        slip44=852,
        bech32_prefix="desmos",
        key_algos=('secp256k1',),
        shortcut="DSM",
        name="Desmos"
    )
    yield NetworkInfo(
        chain_id="dig-1",
        slip44=118,
        bech32_prefix="dig",
        key_algos=('secp256k1', 'ethsecp256k1'),
        shortcut="DIG",
        name="Dig Chain"
    )
    yield NetworkInfo(
        chain_id="echelon_3000-3",
        slip44=60,
        bech32_prefix="echelon",
        key_algos=('secp256k1',),
        shortcut="ECH",
        name="Echelon"
    )
    yield NetworkInfo(
        chain_id="emoney-3",
        slip44=118,
        bech32_prefix="emoney",
        key_algos=('secp256k1',),
        shortcut="NGM",
        name="e-Money"
    )
    yield NetworkInfo(
        chain_id="evmos_9001-2",
        slip44=60,
        bech32_prefix="evmos",
        key_algos=('secp256k1',),
        shortcut="EVMOS",
        name="Evmos"
    )
    yield NetworkInfo(
        chain_id="fetchhub-4",
        slip44=118,
        bech32_prefix="fetch",
        key_algos=('secp256k1',),
        shortcut="FET",
        name="Fetch Hub"
    )
    yield NetworkInfo(
        chain_id="colosseum-1",
        slip44=7777777,
        bech32_prefix="firma",
        key_algos=('secp256k1',),
        shortcut="FCT",
        name="FirmaChain"
    )
    yield NetworkInfo(
        chain_id="galaxy-1",
        slip44=118,
        bech32_prefix="galaxy",
        key_algos=('secp256k1',),
        shortcut="GLX",
        name="Galaxy"
    )
    yield NetworkInfo(
        chain_id="gravity-bridge-3",
        slip44=118,
        bech32_prefix="gravity",
        key_algos=('secp256k1',),
        shortcut="GRAV",
        name="Gravity Bridge"
    )
    yield NetworkInfo(
        chain_id="impacthub-3",
        slip44=118,
        bech32_prefix="ixo",
        key_algos=('secp256k1', 'ed25519'),
        shortcut="IXO",
        name="Impact Hub"
    )
    yield NetworkInfo(
        chain_id="injective-1",
        slip44=60,
        bech32_prefix="inj",
        key_algos=('secp256k1',),
        shortcut="INJ",
        name="Injective"
    )
    yield NetworkInfo(
        chain_id="irishub-1",
        slip44=118,
        bech32_prefix="iaa",
        key_algos=('secp256k1',),
        shortcut="IRIS",
        name="IRISnet"
    )
    yield NetworkInfo(
        chain_id="juno-1",
        slip44=118,
        bech32_prefix="juno",
        key_algos=('secp256k1',),
        shortcut="JUNO",
        name="Juno"
    )
    yield NetworkInfo(
        chain_id="kava-9",
        slip44=118,
        bech32_prefix="kava",
        key_algos=('secp256k1',),
        shortcut="KAVA",
        name="Kava"
    )
    yield NetworkInfo(
        chain_id="kichain-2",
        slip44=118,
        bech32_prefix="ki",
        key_algos=('secp256k1',),
        shortcut="XKI",
        name="Ki"
    )
    yield NetworkInfo(
        chain_id="likecoin-mainnet-2",
        slip44=118,
        bech32_prefix="like",
        key_algos=('secp256k1',),
        shortcut="LIKE",
        name="LikeCoin"
    )
    yield NetworkInfo(
        chain_id="lum-network-1",
        slip44=880,
        bech32_prefix="lum",
        key_algos=('secp256k1',),
        shortcut="LUM",
        name="Lum Network"
    )
    yield NetworkInfo(
        chain_id="meme-1",
        slip44=118,
        bech32_prefix="meme",
        key_algos=('secp256k1',),
        shortcut="MEME",
        name="MEME"
    )
    yield NetworkInfo(
        chain_id="microtick-1",
        slip44=118,
        bech32_prefix="micro",
        key_algos=('secp256k1',),
        shortcut="TICK",
        name="Microtick"
    )
    yield NetworkInfo(
        chain_id="nomic-stakenet",
        slip44=118,
        bech32_prefix="nomic",
        key_algos=('secp256k1',),
        shortcut="nomic",
        name="Nomic Stakenet"
    )
    yield NetworkInfo(
        chain_id="odin-mainnet-freya",
        slip44=118,
        bech32_prefix="odin",
        key_algos=('secp256k1',),
        shortcut="odin",
        name="OdinChain"
    )
    yield NetworkInfo(
        chain_id="Oraichain",
        slip44=118,
        bech32_prefix="orai",
        key_algos=('secp256k1',),
        shortcut="ORAI",
        name="Oraichain"
    )
    yield NetworkInfo(
        chain_id="osmosis-1",
        slip44=118,
        bech32_prefix="osmo",
        key_algos=('secp256k1',),
        shortcut="OSMO",
        name="Osmosis"
    )
    yield NetworkInfo(
        chain_id="panacea-3",
        slip44=371,
        bech32_prefix="panacea",
        key_algos=('secp256k1',),
        shortcut="MED",
        name="Panacea"
    )
    yield NetworkInfo(
        chain_id="core-1",
        slip44=750,
        bech32_prefix="persistence",
        key_algos=('secp256k1',),
        shortcut="XPRT",
        name="Persistence"
    )
    yield NetworkInfo(
        chain_id="pio-mainnet-1",
        slip44=505,
        bech32_prefix="pb",
        key_algos=('secp256k1',),
        shortcut="HASH",
        name="Provenance Blockchain"
    )
    yield NetworkInfo(
        chain_id="regen-1",
        slip44=118,
        bech32_prefix="regen",
        key_algos=('secp256k1',),
        shortcut="REGEN",
        name="Regen Network"
    )
    yield NetworkInfo(
        chain_id="titan-1",
        slip44=118,
        bech32_prefix="rizon",
        key_algos=('secp256k1',),
        shortcut="ATOLO",
        name="RIZON"
    )
    yield NetworkInfo(
        chain_id="secret-4",
        slip44=529,
        bech32_prefix="secret",
        key_algos=('secp256k1',),
        shortcut="SCRT",
        name="Secret Network"
    )
    yield NetworkInfo(
        chain_id="sentinelhub-2",
        slip44=750,
        bech32_prefix="sent",
        key_algos=('secp256k1',),
        shortcut="DVPN",
        name="Sentinel"
    )
    yield NetworkInfo(
        chain_id="shentu-2.2",
        slip44=118,
        bech32_prefix="certik",
        key_algos=('secp256k1',),
        shortcut="CTK",
        name="Shentu"
    )
    yield NetworkInfo(
        chain_id="sifchain-1",
        slip44=118,
        bech32_prefix="sif",
        key_algos=('secp256k1',),
        shortcut="ROWAN",
        name="Sifchain"
    )
    yield NetworkInfo(
        chain_id="sommelier-3",
        slip44=118,
        bech32_prefix="somm",
        key_algos=('secp256k1',),
        shortcut="SOMM",
        name="Sommelier"
    )
    yield NetworkInfo(
        chain_id="stargaze-1",
        slip44=118,
        bech32_prefix="stars",
        key_algos=('secp256k1',),
        shortcut="STARS",
        name="Stargaze"
    )
    yield NetworkInfo(
        chain_id="iov-mainnet-ibc",
        slip44=234,
        bech32_prefix="star",
        key_algos=('secp256k1',),
        shortcut="IOV",
        name="Starname"
    )
    yield NetworkInfo(
        chain_id="columbus-5",
        slip44=330,
        bech32_prefix="terra",
        key_algos=('secp256k1',),
        shortcut="LUNA",
        name="Terra"
    )
    yield NetworkInfo(
        chain_id="thorchain-mainnet-v1",
        slip44=931,
        bech32_prefix="thor",
        key_algos=('secp256k1',),
        shortcut="thorchain",
        name="THORChain"
    )
    yield NetworkInfo(
        chain_id="umee-1",
        slip44=118,
        bech32_prefix="umee",
        key_algos=('secp256k1',),
        shortcut="UMEE",
        name="umee"
    )
    yield NetworkInfo(
        chain_id="vidulum-1",
        slip44=370,
        bech32_prefix="vdl",
        key_algos=('secp256k1',),
        shortcut="VDL",
        name="Vidulum"
    )
