from challenge09 import unpad_pkcs7

BLOCK_SIZE = 16

def strip(string: bytes, block_size = int) -> bytes:
    try:
       return unpad_pkcs7(string, block_size)  
    except Exception as e:
        print(f"{string}:", e)


if __name__ == '__main__':
    base = b"ICE ICE BABY\x04\x04\x04\x04"
    bad_str1 = b"ICE ICE BABY\x05\x05\x05\x05"
    bad_str2 = b"ICE ICE BABY\x01\x02\x03\x04"

    if strip(base, BLOCK_SIZE) != b"ICE ICE BABY":
        raise Exception("What the hell happened?")
    else:
        print(f"\n{base}: SUCCESSFUL PKCS#7 UNPADDING\n")

    strip(bad_str1, BLOCK_SIZE)
    strip(bad_str2, BLOCK_SIZE)

    print("\n-----------------")
    print("ALL TESTS PASSED")
    print("-----------------\n")