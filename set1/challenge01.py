import binascii
import base64 

def base64_convert(hex_value):
    """ 
        We write an exception for any values that are not in hex,
        so we use keyword try and except for a ValueError.
        
        First we "unhex" the value using unhexlify() in the
        binascii library. This returns the binary data of hex value.
        The number of hex characters must be an even value or else
        the binary data is considered incomplete.
        
        We then encode hex_bytes using base64, then decode using
        the decode() function to return a string.
    """
    try:
        hex_bytes = binascii.unhexlify(hex_value)
        b64_bytes = base64.b64encode(hex_bytes)
        b64string = b64_bytes.decode('UTF-8')
        return b64string
        
    except ValueError:
        return "Error, not a hex value."


def main():
    """ 
        main() prompts the user to enter a hexadecimal value.
        We will pull this from cryptopals and copy and paste it in.
        If we wanted we could just put the value in the code. 
    """
    hex_value = input("Enter hex value: ")
    b64_value = base64_convert(hex_value)
    print(b64_value)
    

if __name__ == '__main__':
    main()
