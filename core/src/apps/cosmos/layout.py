from typing import TYPE_CHECKING, Awaitable
from ubinascii import hexlify

from trezor import wire
from trezor.enums import AccessType, ButtonRequestType, MessageType
from trezor.messages import (
    CosmosBankV1beta1MsgSend,
    CosmosBankV1beta1MsgMultiSend,
    CosmwasmWasmV1MsgClearAdmin,
    CosmwasmWasmV1MsgExecuteContract,
    CosmwasmWasmV1MsgInstantiateContract,
    CosmwasmWasmV1MsgMigrateContract,
    CosmwasmWasmV1MsgStoreCode,
    CosmwasmWasmV1MsgUpdateAdmin,
    TerraWasmV1beta1MsgClearContractAdmin,
    TerraWasmV1beta1MsgExecuteContract,
    TerraWasmV1beta1MsgInstantiateContract,
    TerraWasmV1beta1MsgMigrateCode,
    TerraWasmV1beta1MsgMigrateContract,
    TerraWasmV1beta1MsgStoreCode,
    TerraWasmV1beta1MsgUpdateContractAdmin,
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

    # cosmos.bank.*
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

    # cosmwasm.wasm.*, terra.wasm.*
    elif CosmwasmWasmV1MsgClearAdmin.is_type_of(msg):
        type_disp = "Clear admin"
        props = [
            ("From address:", msg.sender),
            ("Contract:", msg.contract)
        ]
    elif TerraWasmV1beta1MsgClearContractAdmin.is_type_of(msg):
        type_disp = "Clear admin"
        props = [
            ("From address:", msg.admin),
            ("Contract:", msg.contract)
        ]

    elif CosmwasmWasmV1MsgUpdateAdmin.is_type_of(msg):
        type_disp = "Update admin"
        props = [
            ("From address:", msg.sender),
            ("New admin:", msg.new_admin),
            ("Contract:", msg.contract)
        ]
    elif TerraWasmV1beta1MsgUpdateContractAdmin.is_type_of(msg):
        type_disp = "Update admin"
        props = [
            ("From address:", msg.admin),
            ("New admin:", msg.new_admin),
            ("Contract:", msg.contract)
        ]

    elif CosmwasmWasmV1MsgExecuteContract.is_type_of(msg):
        type_disp = "Exec. contract"
        props = [
            ("From address:", msg.sender),
            ("Contract:", msg.contract),
            ("Message:", try_decode_bytes(msg.msg))
        ]
        if len(msg.funds) > 0:
            props.append(("Amounts:", format_cosmos_native_amounts(chain_id, msg.funds)))
    elif TerraWasmV1beta1MsgExecuteContract.is_type_of(msg):
        type_disp = "Exec. contract"
        props = [
            ("From address:", msg.sender),
            ("Contract:", msg.contract),
            ("Message:", try_decode_bytes(msg.execute_msg))
        ]
        if len(msg.coins) > 0:
            props.append(("Amounts:", format_cosmos_native_amounts(chain_id, msg.coins)))

    elif CosmwasmWasmV1MsgInstantiateContract.is_type_of(msg):
        type_disp = "Inst. contract"
        props = [
            props.append(("From address:", msg.sender))
        ]
        
        if msg.admin is not None:
            props.append(("Admin:", msg.admin))

        props.append(("Code ID:", msg.code_id))

        if msg.label is not None:
            props.append(("Label:", msg.label))

        props.append(("Init message:", try_decode_bytes(msg.msg)))
        props.append(("Amounts:", format_cosmos_native_amounts(chain_id, msg.funds)))
    elif TerraWasmV1beta1MsgInstantiateContract.is_type_of(msg):
        type_disp = "Inst. contract"
        props = [
            props.append(("From address:", msg.sender))
        ]
        
        if msg.admin is not None:
            props.append(("Admin:", msg.admin))

        props.append(("Code ID:", msg.code_id))
        props.append(("Init message:", try_decode_bytes(msg.init_msg)))
        props.append(("Amounts:", format_cosmos_native_amounts(chain_id, msg.init_coins)))

    elif TerraWasmV1beta1MsgMigrateCode.is_type_of(msg):
        type_disp = "Migrate code"
        props = [
            ("From address:", msg.sender),
            ("Code ID:", msg.code_id),
            ("Code:", msg.wasm_byte_code)
        ]

    elif CosmwasmWasmV1MsgMigrateContract.is_type_of(msg):
        type_disp = "Migr. contract"
        props = [
            ("From address:", msg.sender),
            ("Contract:", msg.contract),
            ("Code ID:", msg.code_id),
            ("Migrate message:", try_decode_bytes(msg.msg))
        ]
    elif TerraWasmV1beta1MsgMigrateContract.is_type_of(msg):
        type_disp = "Migr. contract"
        props = [
            ("From address:", msg.admin),
            ("Contract:", msg.contract),
            ("Code ID:", msg.new_code_id),
            ("Migrate message:", try_decode_bytes(msg.migrate_msg))
        ]

    elif CosmwasmWasmV1MsgStoreCode.is_type_of(msg):
        type_disp = "Store code"
        props = [
            ("From address:", msg.sender),
            ("Code:", msg.wasm_byte_code)
        ]

        if msg.instantiate_permission is not None:
            perm = msg.instantiate_permission.permission
            if perm == AccessType.ACCESS_TYPE_UNSPECIFIED:
                access_disp = "Unspecified"
            elif perm == AccessType.ACCESS_TYPE_NOBODY:
                access_disp = "Nobody"
            elif perm == AccessType.ACCESS_TYPE_ONLY_ADDRESS:
                access_disp = "Address: " + (msg.instantiate_permission.address or "(no addr)")
            elif perm == AccessType.ACCESS_TYPE_EVERYBODY:
                access_disp = "Everybody"
            else:
                raise wire.ProcessError("unknown instantiate_permission permission in cosmwasm.wasm.v1.MsgStoreCode")
                
            props.append(("Permissions:", access_disp))
    elif TerraWasmV1beta1MsgStoreCode.is_type_of(msg):
        type_disp = "Store code"
        props = [
            ("From address:", msg.sender),
            ("Code:", msg.wasm_byte_code)
        ]
    
    # matched nothing
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


def try_decode_bytes(input: bytes) -> str | bytes:
    try:
        return input.decode()
    except UnicodeError:
        return input


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
