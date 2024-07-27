from base64 import b64decode
from os import urandom

import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")
from set1.challenge2v2 import xor1
from set1.challenge7 import decrypt_ecb
from set1.challenge8 import chunks
from set2.challenge09 import unpad_pkcs7
from set3.challenge18 import aes_ctr


key = urandom(16)
BLOCK_SIZE = 16


def exposed_edit(ct: bytes, key: bytes, offset: int, new: bytes) -> bytes:
    start = offset
    end = start + len(new)
    og_pt = decrypt_ecb(ct, key)
    edit_pt = og_pt[:start] + new + og_pt[end:]
    edit_ct = aes_ctr(key, edit_pt)
    return edit_ct


def edit(offset: int, new: bytes) -> bytes:
    return exposed_edit(ct, key, offset, new)


def crack_aesCTR(ct):
    ct_blocked = chunks(ct, BLOCK_SIZE)
    pt = b''
    for i, ct_block in enumerate(ct_blocked):
        ct2 = edit(BLOCK_SIZE*i, b'\00'*BLOCK_SIZE)
        keystream_block = chunks(ct2, BLOCK_SIZE)[i]
        pt_block = xor1(keystream_block, ct_block)
        pt += pt_block
    return unpad_pkcs7(pt, BLOCK_SIZE)


if __name__ == '__main__':
    with open("program_data/25.txt") as file:
        b64_file = file.read()

    _pt = decrypt_ecb(b64decode(b64_file), b"YELLOW SUBMARINE")
    ct = aes_ctr(key, _pt)
    plaintext = crack_aesCTR(ct).decode("ascii")

    print(f"Plaintext: {plaintext}")
