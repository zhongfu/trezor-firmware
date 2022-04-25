from typing import TYPE_CHECKING

from trezor import utils, wire
from trezor.messages import RebootToBootloader, Success

if TYPE_CHECKING:
    from typing import NoReturn


async def reboot_to_bootloader(ctx: wire.Context, msg: RebootToBootloader) -> NoReturn:
    await ctx.write(Success())
    utils.reboot_to_bootloader()
    raise RuntimeError
