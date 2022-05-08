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

from typing import TYPE_CHECKING

from . import messages
from .protobuf import dict_to_proto
from .tools import expect, session

if TYPE_CHECKING:
    from .client import TrezorClient
    from .tools import Address
    from .protobuf import MessageType


@expect(messages.CosmosAddress, field="address", ret_type=str)
def get_address(
    client: "TrezorClient",
    address_n: "Address",
    chain_name: str,
    show_display: bool = False
) -> "MessageType":
    return client.call(
        messages.CosmosGetAddress(
            address_n=address_n,
            chain_name=chain_name,
            show_display=show_display
        )
    )


@expect(messages.CosmosPublicKey, field="public_key", ret_type=bytes)
def get_public_key(
    client: "TrezorClient",
    address_n: "Address",
    chain_name: str,
    show_display: bool = False
) -> "MessageType":
    return client.call(
        messages.CosmosGetPublicKey(
            address_n=address_n,
            chain_name=chain_name,
            show_display=show_display
        )
    )


@session
def sign_tx(
    client: "TrezorClient",
    address_n: "Address", 
    chain_name: str,
    tx_json: dict
) -> messages.CosmosSignedTx:
    msgs = tx_json["msgs"]
    tx_msg = tx_json.copy()
    tx_msg["msg_count"] = len(msgs)
    tx_msg["address_n"] = address_n
    tx_msg["chain_name"] = chain_name
    envelope = dict_to_proto(messages.CosmosSignTx, tx_msg)

    response = client.call(envelope)

    if not isinstance(response, messages.CosmosTxRequest):
        raise RuntimeError(
            "Invalid response, expected CosmosTxRequest, received "
            + type(response).__name__
        )

    sent_count = 0
    for msg in msgs:
        if "type" not in msg:
            raise ValueError("msg has missing type")

        if msg["type"] == "bank/MsgSend":
            proto_msg = dict_to_proto(messages.CosmosMsgSend, msg)
        elif msg["type"] == "bank/MsgMultiSend":
            proto_msg = dict_to_proto(messages.CosmosMsgMultiSend, msg)
        else:
            raise ValueError("unknown msg type")

        response = client.call(proto_msg)
        sent_count += 1

        if sent_count < len(msgs):
            if not isinstance(response, messages.CosmosTxRequest):
                raise RuntimeError(
                    "Invalid response, expected CosmosTxRequest, received "
                    + type(response).__name__
                )
            # else continue
        else: # we've probably already sent all the messages
            if not isinstance(response, messages.CosmosSignedTx):
                raise RuntimeError(
                    "Invalid response, expected CosmosSignedTx, received "
                    + type(response).__name__
                )
            return response
