import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")

from set1.challenge8 import chunks
from set2.challenge09v2 import pad_pkcs7

from Crypto.Cipher import AES
from base64 import b64decode
from collections.abc import Callable
from os import urandom
from itertools import count


BLOCK_SIZE = AES.block_size
KEY_SIZE = 16
ECB_Oracle = Callable[[bytes], bytes]


def constr_oracle() -> ECB_Oracle:
    _key = urandom(KEY_SIZE)
    with open("program_data/12.txt") as f:
        _sec_suffix = b64decode(f.read())

    def oracle_encrypt(pt: bytes) -> bytes:
        pt = pad_pkcs7(pt +_sec_suffix, BLOCK_SIZE)
        cipher = AES.new(_key, AES.MODE_ECB)
        return cipher.encrypt(pt)
        
    return oracle_encrypt


def bs_suff_length(func: ECB_Oracle) -> tuple[int, int]:
    block_size = None
    suffix_length = None
    length = len(func(b'A'))

    for i in count(2):
        length2 = len(func(b'A' * i))
        if length2 > length:
            block_size = length2 - length
            suffix_length = length - i
            break

    assert block_size is not None
    assert suffix_length is not None
    return block_size, suffix_length


def find_byte(pref: bytes, target: bytes, func: ECB_Oracle) -> bytes:
    for b in range(256):
        b = bytes([b])
        messg = pref + b
        block_one = func(messg)[:16]
        if block_one == target:
            return b
    raise Exception("Something went wrong")


def detector(oracle_encrypt):
    ct = oracle_encrypt(bytes(32))
    if ct[:16] == ct[16:32]:
        return True
    raise Exception("Something's amiss")


def main_decrypt(func: ECB_Oracle, suffix_length: int, view_decrypt=False) -> bytes:
    assert detector(func)
    
    ctexts = [chunks(func(bytes(15-n)), BLOCK_SIZE) for n in range(16)]
    shifted = [block for blocks in zip(*ctexts) for block in blocks]
    attack_blocks = shifted[:suffix_length]

    plain = bytes(15)
    for block in attack_blocks:
        plain += find_byte(plain[-15:], block, func)
        if view_decrypt:
            print(plain[15:])
            from time import sleep
            sleep(0.02)
    return plain[15:]


if __name__ == '__main__':
    oracle = constr_oracle()
    block_size, suffix_length = bs_suff_length(oracle)

    print(f"{block_size=}")
    print(f"{suffix_length=}")
    assert block_size == AES.block_size

    pt = main_decrypt(oracle, suffix_length)

    print("\n----------------------\nSUCCESSFUL DECRYPTION\n----------------------")
    print("\nContents of message: \n")
    print(pt.decode('ascii'))
