from base64 import b16decode, b64encode

def hex_to_b64(hex_string1: bytes) -> bytes:
    return b64encode(b16decode(hex_string1, casefold=True))


if __name__ == '__main__':

    hex_string1 = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    b64data = hex_to_b64(hex_string1)

    print("\n", f"{hex_string1=}", "\n")
    print(f"{b64data=}", "\n")
