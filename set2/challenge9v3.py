from Crypto.Util.Padding import pad, unpad

"""

    Same program as v2 but with the pad and unpad functions contained
    in user-defined functions pad_pkcs7() and unpad_pkcs7() with type
    annotations.

"""

def pad_pkcs7(pt: bytes, block_size: int) -> bytes:
    padded_pt = pad(pt, block_size, style='pkcs7')
    return padded_pt
    
    
def unpad_pkcs7(padded: bytes, block_size: int) -> bytes:
    unpadded_pt = unpad(padded, block_size, style='pkcs7')
    return unpadded_pt

  
if __name__ == '__main__':
    
    plaintext = b'YELLOW SUBMARINE'
    pad_pt = pad_pkcs7(plaintext, 20)
    unpad_pt = unpad_pkcs7(pad_pt, len(pad_pt))
    
    if unpad_pt == plaintext:
        print(f"{pad_pt=}")
        print(f"{unpad_pt=}")
        print("\nSuccess, PKCS7 implemented properly.\n")    
    else:
        print("Error. PKCS7 not implemented properly.")
