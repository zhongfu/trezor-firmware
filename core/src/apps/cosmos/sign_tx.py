from trezor import wire
from trezor.crypto.curve import secp256k1
from trezor.crypto.hashlib import sha256
from trezor.enums import MessageType
from trezor.messages import (
    CosmosMsgSend,
    CosmosSignedTx,
    CosmosSignTx,
    CosmosTxRequest,
)

from apps.common import paths
from apps.common.keychain import Keychain, auto_keychain

from . import helpers, layout


@auto_keychain(__name__)
async def sign_tx(
    ctx: wire.Context, envelope: CosmosSignTx, keychain: Keychain
) -> CosmosSignedTx:
    # create transaction message -> sign it -> create signature/pubkey message -> serialize all
    
    # TODO remove
    #if envelope.msg_count > 1:
    #    raise wire.DataError("Multiple messages not supported.")

    await paths.validate_path(ctx, keychain, envelope.address_n)
    node = keychain.derive(envelope.address_n)

    tx_req = CosmosTxRequest()

    msgs = []

    while len(msgs) < envelope.msg_count:
        msg = await ctx.call_any(
            tx_req,
            MessageType.CosmosMsgSend
        )

        if CosmosMsgSend.is_type_of(msg):
            await layout.require_confirm_send(ctx, envelope.chain_id, msg, len(msgs) + 1, envelope.msg_count)
        else:
            raise wire.ProcessError("input message unrecognized")

        msgs.append(msg)

    await layout.require_confirm_memo(ctx, envelope.memo)

    await layout.require_confirm_tx(ctx, envelope.chain_id, envelope.msg_count, envelope.fee.amount)

    msg_pb = helpers.produce_signdoc_bytes_for_signing(node.public_key(), envelope, msgs)

    signature_bytes = generate_content_signature(msg_pb, node.private_key())

    return CosmosSignedTx(signature=signature_bytes, public_key=node.public_key())


def generate_content_signature(json: bytes, private_key: bytes) -> bytes:
    msghash = sha256(json).digest()
    return secp256k1.sign(private_key, msghash)[1:65]
