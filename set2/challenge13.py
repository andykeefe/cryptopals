from os import urandom
from Crypto.Cipher import AES

import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")
from set2.challenge09v2 import pad_pkcs7, unpad_pkcs7

KEY_SIZE = 16
BLOCK_SIZE = AES.block_size
_key = urandom(KEY_SIZE)


def profile_parser(profile: bytes) -> dict[bytes, bytes]:
    kv_pairs = profile.split(b"&")
    parsed = {
        key: value for key, value in [pair.split(b"=") for pair in kv_pairs]
    }


def profile_build(t: tuple[tuple[bytes, bytes], ...]) -> bytes:
    result = b'&'.join(key + b'=' + val for key, val in t)
    return result


def profile_for(email: bytes) -> bytes:
    email.translate(None, b'&=')
    result = profile_build((
        (b'email', email),
        (b'uid', b'10'),
        (b'role', b'user')
        ))
    return result


def enc_prof(email: bytes) -> bytes:
    cipher = AES.new(_key, AES.MODE_ECB)
    profile = profile_for(email)
    return cipher.encrypt(pad_pkcs7(profile, BLOCK_SIZE))


def dec_profile(encrypted: bytes) -> bytes:
    cipher = AES.new(_key, AES.MODE_ECB)
    pt = unpad_pkcs7(cipher.decrypt(encrypted), BLOCK_SIZE)
    return pt


def hack() -> bytes:
    user_1 = b'alev@novy.com'
    user_2 = user_1[:10] + pad_pkcs7(b'admin', BLOCK_SIZE) + user_1[10:]
    
    """ 

        Slice the first 10 bytes of user_1 = b'alev@novy.'
        Add padding to b'admin' up to 16 bytes, concatenate to
        b'alev@novy.' = b'alev@novy.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'.
        Then slice user_1 input from the tenth byte to the end of the byte string, and
        concatenate.
        So user_2 = b'alev@novy.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0bcom'

    """
    
    print(f"{user_1=}\n{user_2=}")
    
    ct_1 = enc_prof(user_1)
    ct_2 = enc_prof(user_2)

    return ct_1[:32] + ct_2[16:32]


if __name__ == '__main__': 
    hacking = hack()
    print("Malicious ct:", hacking)
    print("Decryption:", dec_profile(hacking))
    
