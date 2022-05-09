from typing import TYPE_CHECKING

from trezor.messages import CosmosGetAddress, CosmosAddress
from trezor.ui.layouts import show_address

from apps.common import paths
from apps.common.keychain import Keychain

from . import networks
from .keychain import with_keychain_from_chain_name
from .helpers import address_from_public_key

if TYPE_CHECKING:
    from trezor.wire import Context


@with_keychain_from_chain_name
async def get_address(
    ctx: Context, msg: CosmosGetAddress, keychain: Keychain
) -> CosmosAddress:
    # if chain doesn't exist, then @with_keychain_from_chain_name should catch it
    chain = networks.by_chain_name(msg.chain_name)
    hrp = chain.bech32_prefix

    await paths.validate_path(ctx, keychain, msg.address_n)

    node = keychain.derive(msg.address_n)
    pubkey = node.public_key()
    address = address_from_public_key(pubkey, hrp)
    if msg.show_display:
        title = paths.address_n_to_str(msg.address_n)
        await show_address(ctx, address=address, title=title)

    return CosmosAddress(address=address)
