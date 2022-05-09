from trezor import wire
from trezor.crypto.curve import secp256k1
from trezor.crypto.hashlib import sha256
from trezor.enums import MessageType
from trezor.messages import (
    CosmosSignedTx,
    CosmosSignTx,
    CosmosTxRequest,
)

from apps.common import paths, safety_checks
from apps.common.keychain import Keychain

from . import networks, layout
from .helpers import address_from_public_key, produce_signdoc_bytes_for_signing
from .keychain import with_keychain_from_chain_name


@with_keychain_from_chain_name
async def sign_tx(
    ctx: wire.Context, envelope: CosmosSignTx, keychain: Keychain
) -> CosmosSignedTx:
    # create transaction message -> sign it -> create signature/pubkey message -> serialize all
    
    # TODO remove
    #if envelope.msg_count > 1:
    #    raise wire.DataError("Multiple messages not supported.")

    await paths.validate_path(ctx, keychain, envelope.address_n)
    node = keychain.derive(envelope.address_n)

    # if chain doesn't exist, then @with_keychain_from_chain_name should catch it
    chain = networks.by_chain_name(envelope.chain_name)

    if envelope.chain_id != chain.chain_id:
        if not safety_checks.is_strict():
            raise wire.DataError("Chain ID not known for chain.")
        
        await layout.confirm_chain_id_warning_cosmos(ctx, envelope.chain_id, envelope.chain_name)

    hrp = chain.bech32_prefix
    address = address_from_public_key(node.public_key(), hrp)

    await layout.require_confirm_msg_count_and_from_addr(ctx, envelope.msg_count, address)

    msgs = []

    while len(msgs) < envelope.msg_count:
        msg = await get_next_msg(
            ctx, envelope.chain_id, len(msgs) + 1, envelope.msg_count
        )

        msgs.append(msg)

    await layout.require_confirm_memo(ctx, envelope.memo)

    await layout.require_confirm_tx(ctx, envelope.chain_id, envelope.fee.amount)

    msg_pb = produce_signdoc_bytes_for_signing(node.public_key(), envelope, msgs)

    signature_bytes = generate_content_signature(msg_pb, node.private_key())

    return CosmosSignedTx(signature=signature_bytes, public_key=node.public_key())


async def get_next_msg(
    ctx: wire.Context, chain_id: str, msg_idx: int, msg_count: int
) -> MessageType:
    msg = await ctx.call_any(
        CosmosTxRequest(),
        MessageType.CosmosBankV1beta1MsgSend,
        MessageType.CosmosBankV1beta1MsgMultiSend,
        MessageType.CosmwasmWasmV1MsgClearAdmin,
        MessageType.CosmwasmWasmV1MsgExecuteContract,
        MessageType.CosmwasmWasmV1MsgInstantiateContract,
        MessageType.CosmwasmWasmV1MsgMigrateContract,
        MessageType.CosmwasmWasmV1MsgStoreCode,
        MessageType.CosmwasmWasmV1MsgUpdateAdmin,
        MessageType.TerraWasmV1beta1MsgClearContractAdmin,
        MessageType.TerraWasmV1beta1MsgExecuteContract,
        MessageType.TerraWasmV1beta1MsgInstantiateContract,
        MessageType.TerraWasmV1beta1MsgMigrateCode,
        MessageType.TerraWasmV1beta1MsgMigrateContract,
        MessageType.TerraWasmV1beta1MsgStoreCode,
        MessageType.TerraWasmV1beta1MsgUpdateContractAdmin,
    )

    await layout.require_confirm_cosmos_msg(ctx, chain_id, msg, msg_idx, msg_count)

    return msg


def generate_content_signature(json: bytes, private_key: bytes) -> bytes:
    msghash = sha256(json).digest()
    return secp256k1.sign(private_key, msghash)[1:65]
