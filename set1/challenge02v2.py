a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
b = bytes.fromhex("686974207468652062756c6c277320657965")

def xor1(a, b):
    result = b''
    for byte_1, byte_2 in zip(a, b):
        result += bytes([byte_1 ^ byte_2])

    return bytes(result)


if __name__ == '__main__':

   hex_string = xor1(a, b).hex()
   if hex_string == "746865206b696420646f6e277420706c6179":
       print("Successful XOR")

   else:
       print("Fail")
