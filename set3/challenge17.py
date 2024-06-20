from random import choice
from os import urandom
from base64 import b64decode
from typing import Optional
from Crypto.Cipher import AES

import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")
from set1.challenge8 import chunks
from set1.challenge2v2 import xor1
from set2.challenge09 import pad_pkcs7, unpad_pkcs7

BLOCK_SIZE = AES.block_size
key = urandom(16)
iv = urandom(16)


random_strings = [
    b'MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
    b'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=',
    b'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
    b'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
    b'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
    b'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
    b'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
    b'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=',
    b'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=',
    b'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93'
]

def enc_str(index: Optional[int] = None) -> bytes:
    string = choice(random_strings) if index is None else random_strings[index]
    cipher_obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher_obj.encrypt(pad_pkcs7(string, BLOCK_SIZE))
    return ciphertext


def dec_str(ciphertext: bytes, iv=iv) -> bytes:
    cipher_obj = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher_obj.decrypt(ciphertext)
    return plaintext


def padding_oracle(iv: bytes, ciphertext: bytes) -> bool:
    plaintext = dec_str(ciphertext, iv)
    try:
        unpad_pkcs7(plaintext, BLOCK_SIZE)
    except Exception:
        return False
    return True

def single_block_attack(iv: bytes, block: bytes, oracle) -> bytes:
    pt = b''
    null_iv = [0] * BLOCK_SIZE

    for padding_length in range(1, BLOCK_SIZE+1):
        padding_iv = [padding_length ^ b for b in null_iv]

        for candidate in range(256):
            padding_iv[-padding_length] = candidate
            new_iv = bytes(padding_iv)

            if oracle(new_iv, block):
                if padding_length == 1:
                    padding_iv[-2] ^= 1
                    new_iv = bytes(padding_iv)
                    if not oracle(new_iv, block):
                        continue
                pt = bytes([candidate ^ padding_length]) + pt
                break
        else:
            raise Exception("Something went wrong")

        null_iv[-padding_length] = candidate ^ padding_length

    return xor1(pt, iv)


def attack(ciphertext: bytes, oracle) -> bytes:
    pt = b''
    block_iv = iv
    blocks = chunks(ciphertext, BLOCK_SIZE)
    for i, block in enumerate(blocks):
        pt += single_block_attack(block_iv, block, oracle)
        block_iv = block
    return unpad_pkcs7(pt, BLOCK_SIZE)


if __name__ == '__main__':
    ct = enc_str()
    pt = attack(ct, padding_oracle)
    print(f"\n{pt=}\n")
    print(f"Decoded value: {b64decode(pt).decode('ascii')}\n")



