from Crypto.Util.Padding import pad, unpad

if __name__ == '__main__':
    plaintext = b'YELLOW SUBMARINE'
    pad_pt = pad(plaintext, 20, 'pkcs7')
    unpad_pt = unpad(pad_pt, len(plaintext), 'pkcs7')
   
    if unpad_pt == plaintext:
        print(f"{pad_pt=}")
        print(f"{unpad_pt=}")
        print("\nSuccess. PKCS7 padding and unpadding implemented.\n")
    else:
        print("\nFail. PKCS7 not implemented properly.\n")
