from challenge12 import *
from os.path import commonprefix
import sys
sys.path.append("/home/andy/Documents/Cryptography/cryptopals")


def find_pref_length(oracle: ECB_Oracle, block_size: int) -> int:
    ct_1 = oracle(bytes(16))
    ct_2 = oracle(b'\x0b')

    eq_blocks = len(commonprefix((ct_1, ct_2))) // block_size
    index = block_size * (eq_blocks + 1)

    for i in range(1, 17):
        ct_3 = oracle(bytes(i) + b'\x01')
        if ct_1[:index] == ct_3[:index]:
            return index - i

    raise Exception("Something went wrong")


def beautify_oracle(oracle: ECB_Oracle, prefix_length: int, block_size: int) -> ECB_Oracle:
    pad_len = block_size - (prefix_length % block_size)
    cutoff = prefix_length + pad_len

    def wrapped(message: bytes) -> bytes:
        return oracle(bytes(pad_len) + message)[cutoff:]
    
    return wrapped


if __name__ == '__main__':
    oracle = constr_oracle()
    bs, suffix_length = bs_suff_length(oracle)
    print(f"{bs=}")
    print(f"{suffix_length=}")
    
    if bs != AES.block_size:
        raise Exception("This should never happen")

    prefix_length = find_pref_length(oracle, bs)
    postfix_length = suffix_length - prefix_length
    oracle = beautify_oracle(oracle, prefix_length, bs)
    pt = main_decrypt(oracle, postfix_length)
    print("\n----------------------\nSUCCESSFUL DECRYPTION\n----------------------\n")
    print("Contents of string: \n")
    print(pt.decode("ascii"))
