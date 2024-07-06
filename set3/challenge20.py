from base64 import b64decode
from os import urandom

from challenge18 import aes_ctr
from challenge19v2 import find_keystream

import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals/set1")
from challenge2v2 import xor1


_key = urandom(16)


if __name__ == '__main__':
    with open("program_data/20.txt") as file:
        ciphertexts = [aes_ctr(_key, b64decode(text)) for text in file]

    possible_ks = find_keystream(ciphertexts)

    for i, text in enumerate(ciphertexts):
        pt = xor1(text, possible_ks)
        print(f"{i}: {pt}")
    
    print()

    longest_pt = aes_ctr(_key, ciphertexts[26])
    longest_ct = ciphertexts[26]

    """ 

        Again, just sort of eyeballed the longest line in the ciphertexts list. This time
        I used the enumerate() function to print out the index of the longest line because
        it's not near the beginning or end of the list and I didn't want to count. 

        Ok fine I can't count that high.

    """

    keystream = xor1(longest_ct, longest_pt)
    
    print("-----------------------------------------------------------------------------------------")
    print("Plaintext:\n\n")

    try:
        for text in ciphertexts:
            pt_whole = xor1(text, keystream)
            print(pt_whole.decode())
    except Exception as e:
        print("Something went wrong with the decryption operation.")
        print("Check integrity of the keystream.")
        print(f"Error message: {e}")