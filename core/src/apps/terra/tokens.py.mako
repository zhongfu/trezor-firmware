# generated from tokens.py.mako
# do not edit manually!
# fmt: off
<%
from collections import defaultdict

def group_tokens(tokens):
    r = defaultdict(list)
    for t in sorted(tokens, key=lambda t: t.chain_id):
        r[t.chain_id].append(t)
    return r
%>\

class TokenInfo:
    def __init__(self, symbol: str, decimals: int) -> None:
        self.symbol = symbol
        self.decimals = decimals


UNKNOWN_TOKEN = TokenInfo("Wei UNKN", 0)

NATIVE_TOKEN_NAMES = {
    "luna": "LUNA",
    "aud": "AUT",
    "cad": "CAT",
    "chf": "CHT",
    "cny": "CNT",
    "dkk": "DKT",
    "eur": "EUT",
    "gbp": "GBT",
    "hkd": "HKT",
    "idr": "IDT",
    "inr": "INT",
    "jpy": "JPT",
    "krw": "KRT",
    "mnt": "MNT",
    "myr": "MYT",
    "nok": "NOT",
    "php": "PHT",
    "sdr": "SDT",
    "sek": "SET",
    "sgd": "SGT",
    "usd": "UST"
}


def token_by_native_denom(denom: str) -> TokenInfo:
    token_name = denom[1:]
    if token_name in NATIVE_TOKEN_NAMES:
        return TokenInfo(NATIVE_TOKEN_NAMES[token_name], 6)
    else:
        return TokenInfo(token_name[:-1].upper() + "T", 6)


def token_by_chain_address(chain_id: str, address: str) -> TokenInfo:
## % for token_chain_id, tokens in group_tokens(supported_on("trezor2", cw20)).items():
##     if chain_id == ${token_chain_id}:
##         % for t in tokens:
##         if address == ${black_repr(t.address_bytes)}:
##             return TokenInfo(${black_repr(t.symbol)}, ${t.decimals})  # ${t.chain} / ${t.name.strip()}
##         % endfor
## % endfor
    return UNKNOWN_TOKEN
