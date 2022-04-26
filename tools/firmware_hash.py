#!/usr/bin/env python3

from hashlib import blake2s
from os import sys

FILE_T1 = "legacy/firmware/trezor.bin"
FILE_T2 = "core/build/firmware/firmware.bin"

SIZE_T1 = (7 * 128 + 64) * 1024
SIZE_T2 = 13 * 128 * 1024

for filename, size in ((FILE_T1, SIZE_T1), (FILE_T2, SIZE_T2)):
    try:
        data = open(filename, "rb").read()
    except:
        print(f"{filename} not found")
        continue

    if len(data) > size:
        raise ValueError(fn, f"{filename} too big")
    data = data + b"\xff" * (size - len(data))

    if len(sys.argv) > 1:
        challenge = bytes.fromhex(sys.argv[1])
        firmware_hash = blake2s(data, key=challenge).hexdigest()
    else:
        firmware_hash = blake2s(data).hexdigest()

    print(f"{filename}: {firmware_hash}")
