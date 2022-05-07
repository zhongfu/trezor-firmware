from typing import TYPE_CHECKING

from trezor import wire

from apps.common import paths
from apps.common.keychain import get_keychain

from . import CURVE, PATTERN, networks

if TYPE_CHECKING:
    from typing import Callable, Iterable, TypeVar

    from trezor.messages import (
        CosmosGetAddress,
        CosmosGetPublicKey,
        CosmosSignTx
    )

    from apps.common.keychain import MsgOut, Handler, HandlerWithKeychain

    CosmosMessages = (
        CosmosGetAddress
        | CosmosGetPublicKey
        | CosmosSignTx
    )
    MsgIn = TypeVar("MsgIn", bound=CosmosMessages)


def _schemas_from_chain_name(
    name: str
) -> Iterable[paths.PathSchema]:
    chain = networks.by_chain_name(name)

    if not chain:
        raise wire.DataError("Unsupported chain")
    
    slip44_ids = set((118, chain.slip44))
    
    schemas = [paths.PathSchema.parse(PATTERN, slip44_id) for slip44_id in slip44_ids]
    return [s.copy() for s in schemas]


def with_keychain_from_chain_name(
    func: HandlerWithKeychain[MsgIn, MsgOut]
) -> Handler[MsgIn, MsgOut]:
    async def wrapper(ctx: wire.Context, msg: MsgIn) -> MsgOut:
        schemas = _schemas_from_chain_name(msg.chain_name)
        keychain = await get_keychain(ctx, CURVE, schemas)
        with keychain:
            return await func(ctx, msg, keychain)

    return wrapper
