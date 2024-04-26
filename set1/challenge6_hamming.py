a = b'this is a test'
b = b'wokka wokka!!!'

weights = {n: bin(n).count("1") for n in range(256)}

"""

    The weights variable stores the count of all 1s in a numbers binary
    representation from 0 to 255. For example, the number 10 in binary is
    1010 so there are two 1s. The number 171 in binary is 1010 1011 so it 
    has 5 1s. 

"""

def xor1(a, b):
    result = b''
    for byte_1, byte_2 in zip(a, b):
        result += bytes([byte_1 ^ byte_2])

    # bytes_to_int = int.from_bytes(result, 'big')
    # print(bin(bytes_to_int))
    
    """

        Two lines above will print out the actual binary result of the 
        XOR operation. Not needed for the challenge but educational (?)
        for visualizing the Hamming Distance result.

        bin() can only operate on integers, so you have to take the byte
        string 'result' and convert it to an integer first using the 
        int.from_bytes() function. I used big endian for this because
        I'm used to it but you can use little endian if you want. I am not
        your boss. 
    
    """
   
    return bytes(result)
    
"""

    xor1() can be imported from challenge2v2. XOR operations are useful
    for calculating the Hamming Distance between byte strings because 
    they return 1 if two bits are not the same. Therefore, the Hamming
    Distance between two byte strings can be calculated by counting the 
    number of 1s in the result of their XOR operation.
    
    For example, with a = 1010 0011 and b = 0010 1111, a XOR b = 1000 1100. 
    We have three ones in our result, indicating three differences in bits 
    of a and b, so our Hamming distance is 3. 

"""

def hamming_distance(a: bytes, b: bytes) -> bytes:
    print(sum(weights[byte] for byte in xor1(a, b)))
    
hamming_distance(a, b)

"""

    We've confirmed that our function for calculating the Hamming distance works,
    so we can continue to the actual challenge.

"""
