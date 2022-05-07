from typing import TYPE_CHECKING, Awaitable

from trezor.enums import ButtonRequestType
from trezor.messages import (
    CosmosMsgSend,
    CosmosCoin
)
from trezor.strings import format_amount
from trezor.ui.layouts import confirm_properties, confirm_blob
from trezor.ui.layouts.altcoin import (
    confirm_msg_count_and_signer_addr_cosmos,
    confirm_fee_cosmos,
    confirm_chain_id_warning_cosmos
)

from . import helpers, tokens

if TYPE_CHECKING:
    from trezor.wire import Context


def require_confirm_msg_count_and_from_addr(
    ctx: Context, msg_count: int, address: str
) -> Awaitable[None]:
    return confirm_msg_count_and_signer_addr_cosmos(
        ctx,
        msg_count=str(msg_count),
        address=address
    )

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
    fee: list[CosmosCoin],
) -> Awaitable[None]:
    fee_str = ', '.join((format_cosmos_native_amount(chain_id, coin) for coin in fee))
    return confirm_fee_cosmos(
        ctx,
        fee=fee_str
    )


def show_chain_id_warning(
    ctx: Context,
    chain_id: str,
    chain_name: str
) -> Awaitable[None]:
    return confirm_chain_id_warning_cosmos(
        ctx,
        chain_id,
        chain_name
    )


def format_cosmos_native_amount(chain_id: str, coin: CosmosCoin) -> str:
    token = tokens.token_by_chain_type_tokenid(chain_id, "native", coin.denom)
    value = int(coin.amount)

    return format_cosmos_amount(value, token)


def format_cosmos_amount(value: int, token: tokens.TokenInfo) -> str:
    suffix = token.symbol
    decimals = token.decimals

    if decimals > 6 and value < 10 ** (decimals - 6):
        suffix = "u" + suffix
        decimals = 0

    return f"{format_amount(value, decimals)} {suffix}"
