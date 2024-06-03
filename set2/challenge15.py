import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")
from set2.challenge09v2 import pad_pkcs7, unpad_pkcs7

BLOCK_SIZE = 16

def strip(string: bytes, block_size: int) -> bytes:
    try:
        if unpad_pkcs7(string, block_size) != b'ICE ICE BABY':
            raise Exception("What the hell happened?????")
            pass
        
        else:
            print("-----------------------------------------------------------------------")
            print(f"PASS: PKCS#7 implemented properly for {string}")
            print("-----------------------------------------------------------------------")

    except Exception as e:
        print(f"{string}:", e)


if __name__ == '__main__':
    base_string = b"ICE ICE BABY\x04\x04\x04\x04"
    bad_string1 = b"ICE ICE BABY\x05\x05\x05\x05"
    bad_string2 = b"ICE ICE BABY\x01\x02\x03\x04"
    
    print("")
    strip(base_string, BLOCK_SIZE)
    print("")
    
    strip(bad_string1, BLOCK_SIZE)
    strip(bad_string2, BLOCK_SIZE)
    print("")

""" 

        We use a try and except statement to handle the exceptions that will
        inevitably be raised when trying to strip the padding from bad_strings.
        
        First string passed in is base_string, which we know is good. However, if 
        the stripped version is not our target, we raise an exception, pondering
        how the hell that happened. If it is our target, we neatly print PASS and
        the string we passed in.

        The second and third strings are the nasty ones. The imported unpad_pkcs7
        function uses the unpad function from the PyCryptoDome library, and we know
        it's going to throw an exception for a ValueError, or something like that. 
        To handle these exceptions, we print out the nasty string and the value of the
        exception as e. 

"""
