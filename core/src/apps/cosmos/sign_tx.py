from trezor import wire
from trezor.crypto.curve import secp256k1
from trezor.crypto.hashlib import sha256
from trezor.enums import MessageType
from trezor.messages import (
    CosmosBankV1beta1MsgMultiSend,
    CosmosBankV1beta1MsgSend,
    CosmosSignedTx,
    CosmosSignTx,
    CosmosTxRequest,
)

from apps.common import paths, safety_checks
from apps.common.keychain import Keychain, auto_keychain

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

    tx_req = CosmosTxRequest()

    msgs = []

    while len(msgs) < envelope.msg_count:
        msg = await ctx.call_any(
            tx_req,
            MessageType.CosmosBankV1beta1MsgSend,
            MessageType.CosmosBankV1beta1MsgMultiSend
        )

        if CosmosBankV1beta1MsgSend.is_type_of(msg):
            await layout.require_confirm_send(ctx, envelope.chain_id, msg, len(msgs) + 1, envelope.msg_count)
        elif CosmosBankV1beta1MsgMultiSend.is_type_of(msg):
            await layout.require_confirm_multisend(ctx, envelope.chain_id, msg, len(msgs) + 1, envelope.msg_count)
        else:
            raise wire.ProcessError("input message unrecognized")

        msgs.append(msg)

    await layout.require_confirm_memo(ctx, envelope.memo)

    await layout.require_confirm_tx(ctx, envelope.chain_id, envelope.fee.amount)

    msg_pb = produce_signdoc_bytes_for_signing(node.public_key(), envelope, msgs)

    signature_bytes = generate_content_signature(msg_pb, node.private_key())

    return CosmosSignedTx(signature=signature_bytes, public_key=node.public_key())


def generate_content_signature(json: bytes, private_key: bytes) -> bytes:
    msghash = sha256(json).digest()
    return secp256k1.sign(private_key, msghash)[1:65]
