from Crypto.Util.Padding import pad, unpad

"""

    Padding with PyCryptodome is pretty simple, but takes away
    a lot of the mathematical logic used in the first version of
    this challenge. I'd recommend analyzing that first version to
    get an understanding of padding in terms of modular arithmetic
    because it's always good to practice and apply mathematical 
    concepts when it comes to cryptography.

    I didn't write this code on my native machine so I'm not able
    to test it out yet, but I'm 95% sure it'll work when I access
    a machine with PyCryptodome installed. 

"""

if __name__ == '__main__':
    plaintext = b'YELLOW SUBMARINE'
    pad_pt = pad(plaintext, 20, 'pkcs7')
    
    """

        Pad plaintext to 20 bytes, pass in pkcs7 as padding scheme.
        PKCS #7 is the default so this argument isn't necessary, but
        I threw it in for illustrative purposes. 

    """
    
    unpad_pt = unpad(pad_pt, len(plaintext), 'pkcs7')

    """ 

        Unpad the padded text to the length of original plaintext, 16 bytes.
        Again, PKCS #7 is the default but I passed it in for the sake of it.

    """
   
    if unpad_pt == plaintext:
        print(f"{pad_pt=}")
        print(f"{unpad_pt=}")
        print("\nSuccess. PKCS7 padding and unpadding implemented.\n")
    else:
        print("\nFail. PKCS7 not implemented properly.\n")
