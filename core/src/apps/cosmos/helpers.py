from trezor.enums import SignMode
from micropython import const
from typing import TYPE_CHECKING

from trezor import wire
from trezor.crypto import bech32
from trezor.crypto.scripts import sha256_ripemd160
from trezor.messages import (
    Single,
    CosmosAuthInfo,
    CosmosModeInfo,
    CosmosPublicKey,
    CosmosSignDoc,
    CosmosSignTx,
    CosmosBankV1beta1MsgSend,
    CosmosBankV1beta1MsgMultiSend,
    AnyType,
    CosmosSignerInfo,
    CosmosTx,
    CosmosTxBody
)
from trezor.protobuf import dump_message_buffer

if TYPE_CHECKING:
    from trezor.protobuf import MessageType

def produce_signdoc_bytes_for_signing(public_key: bytes, envelope: CosmosSignTx, msgs: list[MessageType]) -> bytes:
    ser_msgs = list(map(serialize_to_anytype, msgs))
    
    tx_body = CosmosTxBody(
        messages=ser_msgs,
        memo=envelope.memo,
        timeout_height=envelope.timeout_height)

    signer_infos = [
        CosmosSignerInfo(
            public_key=serialize_to_anytype(CosmosPublicKey(value=public_key)),
            mode_info=CosmosModeInfo(single=Single(mode=SignMode.SIGN_MODE_DIRECT)),
            sequence=envelope.sequence
        )
    ]

    auth_info = CosmosAuthInfo(
        signer_infos=signer_infos,
        fee=envelope.fee
    )

    unsigned_tx = CosmosTx(
        body=tx_body,
        auth_info=auth_info
    )

    sign_doc = generate_signdoc(envelope, unsigned_tx)

    return dump_message_buffer(sign_doc)


def serialize_to_anytype(msg: MessageType) -> AnyType:
    if CosmosPublicKey.is_type_of(msg):
        return AnyType(
            type_url="/cosmos.crypto.secp256k1.PubKey",
            value=dump_message_buffer(msg)
        )
    elif CosmosBankV1beta1MsgSend.is_type_of(msg):
        return AnyType(
            type_url="/cosmos.bank.v1beta1.MsgSend",
            value=dump_message_buffer(msg)
        )
    elif CosmosBankV1beta1MsgMultiSend.is_type_of(msg):
        return AnyType(
            type_url="/cosmos.bank.v1beta1.MsgMultiSend",
            value=dump_message_buffer(msg)
        )
    else:
        raise wire.ProcessError("unknown tx message type")


def generate_signdoc(envelope: CosmosSignTx, tx: CosmosTx) -> CosmosSignDoc:
    return CosmosSignDoc(
        body_bytes=dump_message_buffer(tx.body),
        auth_info_bytes=dump_message_buffer(tx.auth_info),
        chain_id=envelope.chain_id,
        account_number=envelope.account_number
    )


def address_from_public_key(pubkey: bytes, hrp: str) -> str:
    """
    Address = RIPEMD160(SHA256(compressed public key))
    Address_Bech32 = HRP + '1' + bech32.encode(convert8BitsTo5Bits(RIPEMD160(SHA256(compressed public key))))
    HRP - cosmos
    """

    h = sha256_ripemd160(pubkey).digest()

    assert (len(h) * 8) % 5 == 0  # no padding will be added by convertbits
    convertedbits = bech32.convertbits(h, 8, 5)
    return bech32.bech32_encode(hrp, convertedbits, bech32.Encoding.BECH32)
