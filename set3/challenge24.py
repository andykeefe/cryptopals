from typing import Optional
from os import urandom
from time import time
from math import ceil

from challenge21v2 import MersenneTwister


msg = b"Fire can't doubt its heat, water can't doubt it's power"


def mersenne_cipher(key: int, pt: bytes, rand_num: Optional[MersenneTwister] = None) -> bytes:
    rand_num = rand_num or MersenneTwister()
    rand_num.seed(key)
    ct = b''

    ks = [rand_num.get_num() for _ in range(ceil(len(pt) / 4))]

    for i, j in enumerate(pt):
        ks_n = ks[i//4]
        ks_b = (ks_n >> 4 * (i % 4)) & 0xFF
        ct += bytes([ks_b ^j])

    return ct

    """ 

            Pass in the sk and pt values derived from get_ct(). We seed the
        Mersenne Twister with the sk (key) value. We generate a keystream ks.
        And we XOR each bytes of pt with the corresponding bytes from ks to 
        produce ciphertext ct. 

    """


def get_ct(message: bytes) -> bytes:
    sk = int.from_bytes(urandom(2), 'big')
    pt = urandom(int.from_bytes(urandom(1), 'big')) + message
    ct = mersenne_cipher(sk, pt)
    return ct

    """ 

        Generates a ciphertext for the given message (msg). 
            We generate a random 16 bit key using urandom() and call that
        sk. We append a more random bytes to the beginning of the message by
        extracting an integer from one random byte and using that integer
        to generate a random number of bytes. 
            For example, lets say urandom(1) gives us 00000 0100. That binary 
        value is equal to 4, so we would generate 4 random bytes to prepend to
        the message and call that concatenation pt. 

    """


def get_token() -> bytes:
    return mersenne_cipher(int(time()), msg)

    """ 

            Generate token by encrypting the msg variable with the current
        timestamp as the key.

    """


def check(token: bytes, quiet=False) -> bool:
    r = MersenneTwister()
    time_current = int(time())
    for t in range(time_current, time_current - (60*60*6), -1):
        cand = mersenne_cipher(t, token, r)
        if cand == msg:
            if not quiet: print("Token was keyed from timestamp -->", t)
            return True
    else:
        return False

    """ 

            Creates a new instance of Mersenne Twister called r.

    """


if __name__ == '__main__':
    ct = get_ct(msg)
    r = MersenneTwister()
    for b in range(2**16):
        if (b % 1024 == 0): print('.', end='', flush=True)
        candidate = mersenne_cipher(b, ct, r)
        if msg in candidate:
            print("\nKey has been found -->", b)
            break

    else:
        raise Exception("Key not found")

    token = get_token()
    print("Token check:", check(token))