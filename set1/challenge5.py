from challenge2v2 import xor1
from itertools import islice, cycle

"""
    
    This example implements another classical cipher, the Vigenere Cipher, where a plaintext is encrypted
    using another word as the key. In this example, our key is the word 'ICE'.

"""

def vigenere_xor(key: bytes, plaintext: bytes) -> bytes:
    full_key = bytes(islice(cycle(key), len(plaintext)))
    return xor1(full_key, plaintext)

"""

    We use two useful iteration functions from the itertools library: islice() and cycle().
    cycle(), for example, takes an input and repeats it. So if our input was 'ICE', 
    using the cycle() function would result in ICEICEICEICEICEICEICE... and so on.

    We use the isclice() function to truncate the cycle() function to the length of the 
    plaintext input. So if we wanted to cut the key to match an input that is 5  characters
    long, we would do something like
                    
                    islice(cycle(key), 5)

    which would result in

                    ICEIC

    as the full key. 

"""



if __name__ == '__main__':
    plaintext = (b"Burning 'em, if you ain't quick and nimble\n"
              b"I go crazy when I hear a cymbal")
    
    """

        Very important to put in the newline character at the end of the first string.
        This matches the input on the cryptopals website. I didn't add the newline
        character and as such I kept failing. For future reference, the new line character
        \n in hex is 0a.

    """

    ciphertext = vigenere_xor(b"ICE", plaintext)
    
    success_cipher = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
                                   "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

    if ciphertext == success_cipher:
        print("\nSUCCESS\n")

    else:
        print("\nFAIL\n")

    print(ciphertext.hex() + "\n")
