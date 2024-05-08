def pkcs7_padding(byte_plaintext: bytes, block_size: int = 16) -> bytes:
    if block_size == 16:
        padding = block_size - (len(byte_plaintext) & 15)
    else:
        padding = block_size - (len(byte_plaintext) % block_size)

    return byte_plaintext + bytes([padding]) * padding

    """ 



    """


if __name__ == '__main__':
    plaintext = b'YELLOW SUBMARINE'
    pad_plaintext = pkcs7_padding(plaintext, block_size = 20)

    print(plaintext)
    print(pad_plaintext)
