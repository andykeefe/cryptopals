import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")
from set1.challenge02v2 import xor1
from set2.challenge09 import pad_pkcs7, unpad_pkcs7

from os import urandom
from Crypto.Cipher import AES

KEY_SIZE = 16
BLOCK_SIZE = AES.block_size
_key = urandom(KEY_SIZE)
iv = urandom(BLOCK_SIZE)



def wrap(data: bytes) -> bytes:
    pref = b"comment1=cooking%20MCs;userdata="
    suff = b";comment2=%20like%20a%20pound%20of%20bacon"

    wrapped = pref + data + suff
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad_pkcs7(wrapped, BLOCK_SIZE))


def check_admin(data: bytes, quiet=True) -> bool:
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    pt = unpad_pkcs7(cipher.decrypt(data), BLOCK_SIZE)
    if not quiet:
        print(f"{pt=}")
    return b";admin=true;" in pt


def adminify() -> bytes:
    one_block = b"A" * BLOCK_SIZE
    ct = wrap(one_block * 2)
    mirror = xor1(one_block, b";admin=true".rjust(BLOCK_SIZE, b"A"))
    padded = mirror.rjust(BLOCK_SIZE*3, b"\x00").ljust(len(ct), b"\x00")
    result_ct = xor1(ct, padded)
    return result_ct


if __name__ == "__main__":
    make_ct = adminify()
    print("Admin? ->", check_admin(make_ct, quiet=True))




