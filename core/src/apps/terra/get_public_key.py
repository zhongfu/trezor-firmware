from typing import TYPE_CHECKING
from ubinascii import hexlify

from trezor.messages import TerraGetPublicKey, TerraPublicKey
from trezor.ui.layouts import show_pubkey

from apps.common import paths
from apps.common.keychain import Keychain, auto_keychain

if TYPE_CHECKING:
    from trezor.wire import Context


@auto_keychain(__name__)
async def get_public_key(
    ctx: Context, msg: TerraGetPublicKey, keychain: Keychain
) -> TerraPublicKey:
    await paths.validate_path(ctx, keychain, msg.address_n)
    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()

    if msg.show_display:
        await show_pubkey(ctx, hexlify(pubkey).decode())

    return TerraPublicKey(public_key=pubkey)
