from typing import TYPE_CHECKING
from ubinascii import hexlify

from trezor.messages import CosmosGetPublicKey, CosmosPublicKey
from trezor.ui.layouts import show_pubkey

from apps.common import paths
from apps.common.keychain import Keychain

from .keychain import with_keychain_from_chain_name

if TYPE_CHECKING:
    from trezor.wire import Context


@with_keychain_from_chain_name
async def get_public_key(
    ctx: Context, msg: CosmosGetPublicKey, keychain: Keychain
) -> CosmosPublicKey:
    await paths.validate_path(ctx, keychain, msg.address_n)
    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()

    if msg.show_display:
        await show_pubkey(ctx, hexlify(pubkey).decode())

    return CosmosPublicKey(public_key=pubkey)
