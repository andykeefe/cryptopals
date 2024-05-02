from base64 import b64decode
from Crypto.Cipher import AES

"""

    Crypto.Cipher is from PyCryptodome. I'm running these exercises on Arch Linux,
    which no longer supports pip. If you're on an Arch machine, you can install 
    PyCryptodome by running sudo pacman -S python-pycryptodome. If you aren't on 
    Arch then ignore this. 

"""


def decrypt_ecb(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

    """

        AES.new instantiates a cipher object, with the first parameter being the key
        we passed in amd the the second parameter being the mode of operation ECB.

        The function returns the decrypted ciphertext. cipher is the object we instantiated,
        decrypt() is a function in PyCryptodome for decryption. 

    """


if __name__ == '__main__':
    with open("program_data/7.txt") as f:
        b64_file = f.read()

    ciphertext = b64decode(b64_file)
    plaintext = decrypt_ecb(ciphertext, b'YELLOW SUBMARINE')

    print(plaintext.replace(b'\n', b''))

    """

        We print out the ciphertext, but first replace the \n byte characters with b''.
        I don't know, I thought this would clean up the plaintext but it didn't do much.
        Once again, you'll see that the plaintext is a classic piece of American literature. 

        I feel like I'm being rickrolled by Vanilla Ice. 

    """
