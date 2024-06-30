from struct import pack
from base64 import b64decode
from collections.abc import Generator
from Crypto.Cipher import AES

import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")
from set1.challenge2v2 import xor1


ciphertext = b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")

def key_stream(key, iv) -> Generator[int, None, None]:
    cipher_obj = AES.new(key, AES.MODE_ECB)
    counter = 0
    ctr_limit = 2**32
    
    for iv in range(0, ctr_limit):
        for counter in range(0, ctr_limit + 1):
            pt = pack('LL', iv, counter)
            ks_block = cipher_obj.encrypt(pt)
            yield from ks_block
            counter = (counter + 1)

    """ 

        Paar and Pelzl (2010) describe this approach to counter mode beautifully:

        "Assume a block cipher with an input width of 128 bits... we choose an IV that is
        a nonce with a length smaller than the block length, e.g. 96 bits. The remaining
        32 bits are then used by a counter... which is initialized to zero. For every block
        that is encrypted... the counter is incremented but the IV stays the same... The number
        of block we can encrypt without choosing a new IV is 2^32... about 32 GB can be encrypted
        before a new IV must be generated" (pp. 132-133). 

        If you debug this program you'll see that the counter (the last 8 bytes of the keystream)
        is incremented every 16 bytes of the plaintext while the IV (the first 8 bytes of the 
        keystream) is not incremented at all. If we were to reach the counter limit, that is, 
        about 32 GB of data, the IV would increment by 1, and the counter would reset. 

        Is this a good implementation? I have no idea, but I surely won't be encrypted 32 GB of data
        with this program so it serves its purpose just fine so long as we can derive the plaintext. 

    """


def aes_ctr(key: bytes, ct: bytes, iv: int = 0) -> bytes:
    return xor1(ct, key_stream(key, iv))

    """

        In counter mode, the plaintext/ciphertext isn't an input to the block cipher. Instead
        you develop a keystream by concatenating an initialization vector and counter, 
        encrypting the result, and XORing it with the plaintext. 

    """


if __name__ == '__main__':
    try:
        plaintext = aes_ctr(b"YELLOW SUBMARINE", ciphertext).decode()
        
        print("\nPlaintext:\n-----------------------------------------------------")
        print(plaintext)
        print("-----------------------------------------------------\n")

    except Exception as e:
        print("Something went wrong -->", e)
