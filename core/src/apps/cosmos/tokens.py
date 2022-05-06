# generated from tokens.py.mako
# do not edit manually!
# fmt: off

class TokenInfo:
    def __init__(self, symbol: str, decimals: int) -> None:
        self.symbol = symbol
        self.decimals = decimals


UNKNOWN_TOKEN = TokenInfo("UNKN", 0)


def token_by_native_denom(chain_id: str, denom: str) -> TokenInfo:
    return TokenInfo(denom, 0)

def token_by_chain_address(chain_id: str, address: str) -> TokenInfo:
    return UNKNOWN_TOKEN
