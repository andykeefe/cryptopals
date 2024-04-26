import operator

def main():
    """
        Start by defining our two values to be XORed, and the intended
        result of the operation. 
    
        Then decode the hex values a and b into bytes using the 
        bytes.fromhex() operation. 
    
        Then use the use operator.xor on the converted values, containing
        it in the map() function that returns an interator. Use the bytes()
        function on the whole operation to keep the result in bytes.
    
        Then convert the XORed value back to hexadecimal, print it,
        and use conditional operators to check the end result is equal
        to the intended result c.
    """
    
    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"
    c = "746865206b696420646f6e277420706c6179"
    
    hex_bytesA = bytes.fromhex(a)
    hex_bytesB = bytes.fromhex(b)
    
    end_value = bytes(map(operator.xor, hex_bytesA, hex_bytesB))
    xor_value = end_value.hex()
    print(xor_value)
    
    if xor_value == c:
        print("Well done")
        
    else:
        print("WRONGGGGG")
    
    
if __name__ == '__main__':
    main()
