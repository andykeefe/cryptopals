
import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")

"""

    I have problem sets contained in different directories, i.e. 
    /cryptopals/set1, /cryptopals/set2, and so on. We need to import
    functions from other directories frequently. To do this we append
    the system path to cryptopals parent directory. 

""" 

from set1.challenge2v2 import xor1
from set1.challenge7 import decrypt_ecb, AES
from set1.challenge8 import chunks
from base64 import b64decode


BLOCK_SIZE = AES.block_size  # 16 byte block size

def cbc(iv: bytes, key: bytes, ct: bytes) -> bytes:
    ct_blocks = chunks(ct, BLOCK_SIZE)

    """

        Ciphertext is broken up into chunks of 16 bytes using the
        chunks() function from challenge 8, which has a good comment
        about how the function works. 

    """
    prev_ct = iv
    pt = b''
    for ct_block in ct_blocks:
        dec = decrypt_ecb(ct_block, key)
        pt += xor1(dec, prev_ct)
        prev_ct = ct_block

        """

            Here is the main logic of CBC decryption. We start knowing that 
            the ciphertext is broken up into blocks of size 16 bytes. We
            create a for loop to iterate through block of the ciphertext.

            Each block is decrypted using the same key, and we store the
            result of each block in variable dec. Then we initially XOR the 
            first block with the IV, in this case, 16 null bytes. This is the
            first decrypted block. 

            Because we're in CBC mode, subsequent blocks are XORed with the 
            previous ciphertext block, so we "replace" the inital 16 null byte
            IV with the previous ciphertext block. This process repeats until
            we have iterated through the entire ciphertext. 

            I'd recommend running a debugger once this program is functional
            to get a better understanding of how CBC works. It's a lot of fun.

        """
    return pt

if __name__ == '__main__':

    key = b'YELLOW SUBMARINE'
    iv = bytes(BLOCK_SIZE)  # initialize 16 null bytes

    with open("program_data/10.txt") as f:
        b64_file = f.read()

    ct = b64decode(b64_file)
    pt = cbc(iv, key, ct)

    print(pt.decode('ascii'))

    """ 

        Once again, we have been Vanilla Iced. How long must we endure his wrath?

    """

