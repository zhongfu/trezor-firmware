# generated from tokens.py.mako
# do not edit manually!
# fmt: off

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
    return UNKNOWN_TOKEN
