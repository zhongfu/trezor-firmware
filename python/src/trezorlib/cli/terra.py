# This file is part of the Trezor project.
#
# Copyright (C) 2012-2022 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import json
from typing import TYPE_CHECKING, TextIO

import click

from .. import terra, tools
from . import with_client

if TYPE_CHECKING:
    from .. import messages
    from ..client import TrezorClient


PATH_HELP = "BIP-32 path to key, e.g. m/44'/330'/0'/0/0"


@click.group(name="terra")
def cli() -> None:
    """Terra commands."""


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@with_client
def get_address(client: "TrezorClient", address: str, show_display: bool) -> str:
    """Get Terra address for specified path."""
    address_n = tools.parse_path(address)
    return terra.get_address(client, address_n, show_display)


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@with_client
def get_public_key(client: "TrezorClient", address: str, show_display: bool) -> str:
    """Get Terra public key."""
    address_n = tools.parse_path(address)
    return terra.get_public_key(client, address_n, show_display).hex()


@cli.command()
@click.argument("file", type=click.File("r"))
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-f", "--file", "_ignore", is_flag=True, hidden=True, expose_value=False)
@with_client
def sign_tx(
    client: "TrezorClient", address: str, file: TextIO
) -> "messages.TerraSignedTx":
    """Sign Terra transaction.

    Transaction must be provided as a JSON file.
    """
    address_n = tools.parse_path(address)
    return terra.sign_tx(client, address_n, json.load(file))
