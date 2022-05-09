from typing import TYPE_CHECKING, Awaitable

from trezor import wire
from trezor.enums import ButtonRequestType, MessageType
from trezor.messages import (
    CosmosBankV1beta1MsgSend,
    CosmosBankV1beta1MsgMultiSend,
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


def require_confirm_generic(
    ctx: Context, msg_disp_name: str, props: list[tuple[str, str]], msg_idx: int, msg_count: int
) -> Awaitable[None]:
    return confirm_properties(
        ctx,
        "confirm_generic",
        title=f"({msg_idx}/{msg_count}) {msg_disp_name}",
        props=props,
        br_code=ButtonRequestType.ConfirmOutput
    )


def require_confirm_cosmos_msg(
    ctx: Context, chain_id: str, msg: MessageType, msg_idx: int, msg_count: int
) -> Awaitable[None]:
    if CosmosBankV1beta1MsgSend.is_type_of(msg):
        type_disp = "Send"
        props = [
            ("From address:", msg.from_address),
            ("To address:", msg.to_address),
            ("Amounts:", format_cosmos_native_amounts(chain_id, msg.amounts)),
        ]
    elif CosmosBankV1beta1MsgMultiSend.is_type_of(msg):
        type_disp = "Send"
        props = []

        input_count = 0
        input_len = len(msg.inputs)
        for input in msg.inputs:
            input_count += 1
            progress = f"({input_count}/{input_len})"
            props.append((f"{progress} Input address:", input.address))
            props.append((f"{progress} Input amounts:", format_cosmos_native_amounts(chain_id, input.amounts)))

        output_count = 0
        output_len = len(msg.outputs)
        for output in msg.outputs:
            output_count += 1
            progress = f"({output_count}/{output_len})"
            props.append((f"{progress} Output address:", output.address))
            props.append((f"{progress} Output amounts:", format_cosmos_native_amounts(chain_id, output.amounts)))
    else:
        raise wire.ProcessError("input message unrecognized")

    return require_confirm_generic(
        ctx, type_disp, props, msg_idx, msg_count
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


def format_cosmos_native_amounts(chain_id: str, coins: list[CosmosCoin]) -> str:
    return ', '.join(
        format_cosmos_native_amount(chain_id, coin) for coin in coins
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
