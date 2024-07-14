from os import urandom
from challenge21v2 import MersenneTwister

l = 18
t, c = 15, 0xEFC60000
s, b = 7, 0x9D2C5680
u = 11

""" 

    These are some of the parameters from the Mersenne Twister 
    implemented in challenge 21. They are used to "undo" the 
    tempering operations 

"""


def untemper(num: int) -> int:
    num ^= num >> l
    num ^= (num << t) & c

    block = num & 0x7F
    invert = block

    for i in range(1, 5):
        block = (block & (b >> (s*i))) ^ (num >> (s*i)) & 0x7F
        invert  += block << (s*i)
    num = invert

    block1 = num & 0xFFE00000
    block2 = (num ^ (block1 >> u)) & 0x001FFC00
    block3 = (num ^ (block2 >> u)) & 0x000003FF
    
    num = block1 + block2 + block3

    return num



def cloneMT(rng: MersenneTwister) -> MersenneTwister:
    generated = [rng.get_num() for _ in range(624)]
    state = [untemper(value) for value in generated]

    fresh_rng = MersenneTwister()
    fresh_rng.index = fresh_rng.n
    fresh_rng.state = state

    return fresh_rng


if __name__ == '__main__':
    for _ in range(10):
        random1 = MersenneTwister()
        random1.seed(int.from_bytes(urandom(4), 'big'))
        random2 = cloneMT(random1)

        try:
            assert random2 is not random1
            assert random2.state == random1.state

            for _ in range(10**3):
                assert random1.get_num() == random2.get_num()
            
            print(".", end="", flush=True)

        except Exception as e:
            print("   Failed to clone MT19937")
            print("      Error -->", e)

    print("\nCLONING OPERATION SUCCESSFUL")

