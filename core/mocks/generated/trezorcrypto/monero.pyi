from typing import *


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
class Point:
    """
    EC point on ED25519
    """
    def __init__(self, x: Point | bytes | None = None):
        """
        Constructor
        """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
class Scalar:
    """
    EC scalar on SC25519
    """
    def __init__(self, x: Scalar | bytes | int | None = None):
        """
        Constructor
        """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
class Hasher:
    """
    XMR hasher
    """
    def __init__(self, x: bytes | None = None):
        """
        Constructor
        """
    def update(self, buffer: bytes) -> None:
        """
        Update hasher
        """
    def digest(self) -> bytes:
        """
        Computes digest
        """
    def copy(self) -> Hasher:
        """
        Creates copy of the hasher, preserving the state
        """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def init256_modm(
    dst: Scalar | None, val: int | bytes | Scalar
) -> Scalar:
    """
    Initializes a scalar
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def check256_modm(val: Scalar) -> None:
    """
    Throws exception if scalar is invalid
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def iszero256_modm(val: Scalar) -> bool:
    """
    Returns False if the scalar is zero
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def eq256_modm(a: Scalar, b: Scalar) -> int:
    """
    Compares scalars, returns 1 on the same value
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def add256_modm(r: Scalar | None, a: Scalar, b: Scalar) -> Scalar:
    """
    Scalar addition
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def sub256_modm(r: Scalar | None, a: Scalar, b: Scalar) -> Scalar:
    """
    Scalar subtraction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def mul256_modm(r: Scalar | None, a: Scalar, b: Scalar) -> Scalar:
    """
    Scalar multiplication
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def mulsub256_modm(
    r: Scalar | None, a: Scalar, b: Scalar, c: Scalar
) -> Scalar:
    """
    c - a*b
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def muladd256_modm(
    r: Scalar | None, a: Scalar, b: Scalar, c: Scalar
) -> Scalar:
    """
    c + a*b
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def inv256_modm(r: Scalar | None, a: Scalar) -> Scalar:
    """
    Scalar modular inversion
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def pack256_modm(
    r: bytes | None, a: Scalar, offset: int | None = 0
) -> bytes:
    """
    Scalar compression
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def unpack256_modm(
    r: Scalar | None, a: bytes, offset: int = 0
) -> Scalar:
    """
    Scalar decompression
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def unpack256_modm_noreduce(
    r: Scalar | None, a: bytes, offset: int = 0
) -> Scalar:
    """
    Scalar decompression, raw, without modular reduction
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_set_neutral(r: Point | None = None) -> Point:
    """
    Sets neutral point
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_set_xmr_h(r: Point | None = None) -> Point:
    """
    Sets H point
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_check(r: Point) -> None:
    """
    Checks point, throws if not on curve
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_eq(a: Point, b: Point) -> bool:
    """
    Compares EC points
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_add(r: Point | None, a: Point, b: Point) -> Point:
    """
    Adds EC points
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_sub(r: Point | None, a: Point, b: Point) -> Point:
    """
    Subtracts EC points
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_mul8(r: Point | None, p: Point) -> Point:
    """
    EC point * 8
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_double_scalarmult_vartime(
    r: Point | None, p1: Point, s1: Scalar, s2: Scalar
) -> Point:
    """
    s1 * G + s2 * p1
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_double_scalarmult_vartime2(
    r: Point | None,
    p1: Point,
    s1: Scalar,
    p2: Point,
    s2: Scalar,
) -> Point:
    """
    s1 * p1 + s2 * p2
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_scalarmult_base(
    r: Point | None, s: Scalar | int
) -> Point:
    """
    s * G
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_scalarmult(
    r: Point | None, p: Point, s: Scalar | int
) -> Point:
    """
    s * p
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_pack(r: bytes | None, p: Point, offset: int = 0) -> bytes:
    """
    Point compression
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ge25519_unpack_vartime(
    r: Point | None, buff: bytes, offset: int = 0
) -> Point:
    """
    Point decompression
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_base58_addr_encode_check(tag: int, buff: bytes) -> str:
    """
    Monero block base 58 encoding
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_base58_addr_decode_check(buff: bytes) -> tuple[bytes, int]:
    """
    Monero block base 58 decoding, returning (decoded, tag) or raising on
    error.
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_random_scalar(r: Scalar | None = None) -> Scalar:
    """
    Generates a random scalar
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_fast_hash(
   r: bytes | None,
   buff: bytes,
   length: int | None = None,
   offset: int = 0,
) -> bytes:
    """
    XMR fast hash
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_hash_to_ec(
    r: Point | None,
    buff: bytes,
    length: int | None = None,
    offset: int = 0,
) -> Point:
    """
    XMR hashing to EC point
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_hash_to_scalar(
   r: Scalar | None,
   buff: bytes,
   length: int | None = None,
   offset: int = 0,
) -> Scalar:
    """
    XMR hashing to EC scalar
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_derivation_to_scalar(
    r: Scalar | None, p: Point, output_index: int
) -> Scalar:
    """
    H_s(derivation || varint(output_index))
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_generate_key_derivation(
    r: Point | None, A: Point, b: Scalar
) -> Point:
    """
    8*(key2*key1)
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_derive_private_key(
    r: Scalar | None, deriv: Point, idx: int, base: Scalar
) -> Scalar:
    """
    base + H_s(derivation || varint(output_index))
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_derive_public_key(
    r: Point | None, deriv: Point, idx: int, base: Point
) -> Point:
    """
    H_s(derivation || varint(output_index))G + base
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_add_keys2(
    r: Point | None, a: Scalar, b: Scalar, B: Point
) -> Point:
    """
    aG + bB, G is basepoint
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_add_keys2_vartime(
    r: Point | None, a: Scalar, b: Scalar, B: Point
) -> Point:
    """
    aG + bB, G is basepoint
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_add_keys3(
    r: Point | None, a: Scalar, A: Point, b: Scalar, B: Point
) -> Point:
    """
    aA + bB
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_add_keys3_vartime(
    r: Point | None, a: Scalar, A: Point, b: Scalar, B: Point
) -> Point:
    """
    aA + bB
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_get_subaddress_secret_key(
    r: Scalar | None, major: int, minor: int, m: Scalar
) -> Scalar:
    """
    Hs(SubAddr || a || index_major || index_minor)
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def xmr_gen_c(r: Point | None, a: Scalar, amount: int) -> Point:
    """
    aG + amount * H
    """


# extmod/modtrezorcrypto/modtrezorcrypto-monero.h
def ct_equals(a: bytes, b: bytes) -> bool:
    """
    Constant time buffer comparison
    """
