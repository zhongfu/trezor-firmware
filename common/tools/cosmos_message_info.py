#!/usr/bin/env python3
import json
import os

from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent

if os.environ.get("DEFS_DIR"):
    DEFS_DIR = Path(os.environ.get("DEFS_DIR")).resolve()
else:
    DEFS_DIR = ROOT / "defs"


def load_json(*path):
    """Convenience function to load a JSON file from DEFS_DIR."""
    if len(path) == 1 and isinstance(path[0], Path):
        file = path[0]
    else:
        file = Path(DEFS_DIR, *path)

    return json.loads(file.read_text(), object_pairs_hook=OrderedDict)


def get_cosmos_message_mapping() -> dict[str, str]:
    """
    returns a dict mapping from type_url to (autogenerated) protobuf message name

    the protobuf message with the autogenerated name may not exist
    """
    return load_json("cosmos/message-mapping.json")
