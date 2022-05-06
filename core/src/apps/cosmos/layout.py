from typing import TYPE_CHECKING, Awaitable
from . import tokens

from trezor.enums import ButtonRequestType
from trezor.messages import (
    CosmosMsgSend,
    CosmosCoin
)
from trezor.strings import format_amount
from trezor.ui.layouts import confirm_properties, confirm_blob
from trezor.ui.layouts.altcoin import confirm_tx_cosmos

from . import helpers

if TYPE_CHECKING:
    from trezor.wire import Context

def require_confirm_send(ctx: Context, chain_id: str, msg: CosmosMsgSend, msg_idx: int, msg_count: int) -> Awaitable[None]:
    coins_fmt = (format_cosmos_native_amount(chain_id, coin) for coin in msg.amounts)
    props = [
        ("To address:", msg.to_address),
        ("Amounts:", ', '.join(coins_fmt)),
    ]

    return confirm_properties(
        ctx,
        "confirm_amount",
        title=f"({msg_idx}/{msg_count}) Confirm send",
        props=props,
        br_code=ButtonRequestType.ConfirmOutput
    )


def require_confirm_memo(ctx: Context, memo_text: str) -> Awaitable[None]:
    return confirm_blob(
        ctx=ctx,
        br_type="confirm_memo",
        title="Confirm memo",
        description="Memo" if memo_text is not None else "No memo!",
        data=memo_text or ''
    )


def require_confirm_tx(
    ctx: Context,
    chain_id: str,
    msg_count: int,
    fee: list[CosmosCoin],
) -> Awaitable[None]:
    fee_str = ', '.join((format_cosmos_native_amount(chain_id, coin) for coin in fee))
    return confirm_tx_cosmos(
        ctx,
        str(msg_count),
        fee=fee_str
    )


def format_cosmos_native_amount(chain_id: str, coin: CosmosCoin) -> str:
    token = tokens.token_by_native_denom(chain_id, coin.denom)
    value = int(coin.amount)

    return format_cosmos_amount(value, token)


def format_cosmos_amount(value: int, token: tokens.TokenInfo) -> str:
    suffix = token.symbol
    decimals = token.decimals

    if decimals > 6 and value < 10 ** (decimals - 6):
        suffix = "u" + suffix
        decimals = 0

    return f"{format_amount(value, decimals)} {suffix}"
