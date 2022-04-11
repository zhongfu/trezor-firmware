# Author: Dusan Klinec, ph4r05, 2018
#
# Resources:
# https://cr.yp.to
# https://github.com/monero-project/mininero
# https://godoc.org/github.com/agl/ed25519/edwards25519
# https://tools.ietf.org/html/draft-josefsson-eddsa-ed25519-00#section-4
# https://github.com/monero-project/research-lab

from trezor.crypto import monero as tcry, random
from trezor.crypto.hashlib import sha3_256

Scalar = tcry.Scalar
Point = tcry.Point
NULL_KEY_ENC = b"\x00" * 32

random_bytes = random.bytes
ct_equals = tcry.ct_equals


def get_keccak(data: bytes | None = None) -> sha3_256:
    return sha3_256(data=data, keccak=True)


fast_hash_into = tcry.xmr_fast_hash


def keccak_2hash(inp: bytes, buff: bytes | None = None) -> bytes:
    buff = buff if buff else bytearray(32)
    fast_hash_into(buff, inp)
    fast_hash_into(buff, buff)
    return buff


def compute_hmac(key: bytes, msg: bytes) -> bytes:
    digestmod = get_keccak
    inner = digestmod()
    block_size = inner.block_size
    if len(key) > block_size:
        key = digestmod(key).digest()
    key_block = bytearray(block_size)
    for i in range(block_size):
        key_block[i] = 0x36
    for i in range(len(key)):
        key_block[i] ^= key[i]
    inner.update(key_block)
    inner.update(msg)
    outer = digestmod()
    for i in range(block_size):
        key_block[i] = 0x5C
    for i in range(len(key)):
        key_block[i] ^= key[i]
    outer.update(key_block)
    outer.update(inner.digest())
    return outer.digest()


#
# EC
#


decodepoint_into = tcry.ge25519_unpack_vartime
encodepoint_into = tcry.ge25519_pack

decodeint_into_noreduce = tcry.unpack256_modm_noreduce
decodeint_into = tcry.unpack256_modm
encodeint_into = tcry.pack256_modm

check_ed25519point = tcry.ge25519_check

scalarmult_base_into = tcry.ge25519_scalarmult_base
scalarmult_into = tcry.ge25519_scalarmult

point_add_into = tcry.ge25519_add
point_sub_into = tcry.ge25519_sub
point_eq = tcry.ge25519_eq


def decodepoint(x: bytes) -> Point:
    return decodepoint_into(None, x)


def encodepoint(x: Point, offset: int = 0) -> bytes:
    return encodepoint_into(None, x, offset)


def encodeint(x: Scalar, offset: int = 0) -> bytes:
    return encodeint_into(None, x, offset)


def decodeint(x: bytes) -> Scalar:
    return decodeint_into(None, x)


INV_EIGHT = b"\x79\x2f\xdc\xe2\x29\xe5\x06\x61\xd0\xda\x1c\x7d\xb3\x9d\xd3\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06"
INV_EIGHT_SC = decodeint(INV_EIGHT)


#
# Zmod(order), scalar values field
#


sc_copy = tcry.init256_modm
sc_check = tcry.check256_modm

sc_add_into = tcry.add256_modm
sc_sub_into = tcry.sub256_modm
sc_mul_into = tcry.mul256_modm

sc_iszero = tcry.iszero256_modm

sc_eq = tcry.eq256_modm
sc_mulsub_into = tcry.mulsub256_modm
sc_muladd_into = tcry.muladd256_modm
sc_inv_into = tcry.inv256_modm

random_scalar = tcry.xmr_random_scalar


#
# GE - ed25519 group
#
ge25519_double_scalarmult_vartime_into = tcry.ge25519_double_scalarmult_vartime


identity_into = tcry.ge25519_set_neutral

"""
https://www.imperialviolet.org/2013/12/25/elligator.html
http://elligator.cr.yp.to/
http://elligator.cr.yp.to/elligator-20130828.pdf
"""

#
# Monero specific
#

hash_to_scalar_into = tcry.xmr_hash_to_scalar


# H_p(buf)
#
# Code adapted from MiniNero: https://github.com/monero-project/mininero
# https://github.com/monero-project/research-lab/blob/master/whitepaper/ge_fromfe_writeup/ge_fromfe.pdf
# http://archive.is/yfINb
hash_to_point_into = tcry.xmr_hash_to_ec


#
# XMR
#


xmr_H = tcry.ge25519_set_xmr_h


add_keys2_into = tcry.xmr_add_keys2_vartime
add_keys3_into = tcry.xmr_add_keys3_vartime
gen_commitment_into = tcry.xmr_gen_c


def generate_key_derivation(pub: Point, sec: Scalar) -> Point:
    """
    Key derivation: 8*(key2*key1)
    """
    sc_check(sec)  # checks that the secret key is uniform enough...
    check_ed25519point(pub)
    return tcry.xmr_generate_key_derivation(None, pub, sec)


def derivation_to_scalar(derivation: Point, output_index: int) -> Scalar:
    """
    H_s(derivation || varint(output_index))
    """
    check_ed25519point(derivation)
    return tcry.xmr_derivation_to_scalar(None, derivation, output_index)


def derive_public_key(derivation: Point, output_index: int, B: Point) -> Point:
    """
    H_s(derivation || varint(output_index))G + B
    """
    check_ed25519point(B)
    return tcry.xmr_derive_public_key(None, derivation, output_index, B)


def derive_secret_key(derivation: Point, output_index: int, base: Scalar) -> Scalar:
    """
    base + H_s(derivation || varint(output_index))
    """
    sc_check(base)
    return tcry.xmr_derive_private_key(None, derivation, output_index, base)


def get_subaddress_secret_key(
    secret_key: Scalar, major: int = 0, minor: int = 0
) -> Scalar:
    """
    Builds subaddress secret key from the subaddress index
    Hs(SubAddr || a || index_major || index_minor)
    """
    return tcry.xmr_get_subaddress_secret_key(None, major, minor, secret_key)


def generate_signature(data: bytes, priv: Scalar) -> tuple[Scalar, Scalar, Point]:
    """
    Generate EC signature
    crypto_ops::generate_signature(const hash &prefix_hash, const public_key &pub, const secret_key &sec, signature &sig)
    """
    pub = scalarmult_base_into(None, priv)

    k = random_scalar()
    comm = scalarmult_base_into(None, k)

    buff = data + encodepoint(pub) + encodepoint(comm)
    c = hash_to_scalar_into(None, buff)
    r = sc_mulsub_into(None, priv, c, k)
    return c, r, pub


def check_signature(data: bytes, c: Scalar, r: Scalar, pub: Point) -> bool:
    """
    EC signature verification
    """
    check_ed25519point(pub)
    if sc_check(c) != 0 or sc_check(r) != 0:
        raise ValueError("Signature error")

    tmp2 = point_add_into(
        None, scalarmult_into(None, pub, c), scalarmult_base_into(None, r)
    )
    buff = data + encodepoint(pub) + encodepoint(tmp2)
    tmp_c = hash_to_scalar_into(None, buff)
    res = sc_sub_into(None, tmp_c, c)
    return sc_iszero(res)


def xor8(buff: bytearray, key: bytes) -> bytes:
    for i in range(8):
        buff[i] ^= key[i]
    return buff
