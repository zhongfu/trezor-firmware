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


UNKNOWN_TOKEN = TokenInfo("uUNKN", 0)


def token_by_chain_type_tokenid(chain_id: str, token_type: str, token_id: str) -> TokenInfo:
% for token_chain_id, tokens in group_tokens(supported_on("trezor2", cw20)).items():
    if chain_id == "${token_chain_id}":
        % for t in tokens:
        if token_type == "${t.token_type}" and token_id == "${t.token_id}":
            return TokenInfo(${black_repr(t.symbol)}, ${t.decimals})  # ${t.chain} / ${t.name.strip()}
        % endfor
% endfor
    return UNKNOWN_TOKEN
