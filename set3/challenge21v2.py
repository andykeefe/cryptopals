from os import urandom


class MersenneError(Exception): pass


class MersenneTwister:
    w, n, m, r = 32, 624, 397, 31
    a = 0x990BB0DF

    """  

        The period parameters determining the period --
            w: word size in number of bits
            n: degree of recursion
            m: middle term
            r: separation point of one word
            a: vector parameter
    
    """

    u, d = 11, 0xFFFFFFFF
    l = 18

    """ 

        u, d, l: additional MT tempering bit shifts/masks

    """

    s, b = 7, 0x9D2C5680
    t, c = 15, 0xEFC60000
    
    f = 1812433253

    """ 

        s, t: twisted generalized feedback shift register of 
            rational normal form (TGFSR(R)) tempering bit shifts

        b, c: TGFSR(R) tempering bitmasks

        f: constant multiplier used in seeding

    """

    
    int_mask = 0xFFFFFFFF
    
    index = n+1
    
    lower_mask = 0x7FFFFFFF
    upper_mask = 0x80000000

    def __init__(self):
        self.state = [0]*self.n

        """ 

                Initialization, initial state is 'n' zeros, where n is 
            a period paramter integer 624.

        """


    def seed(self, seed_value: int) -> None:
        self.index = self.n

        self.state[0] = seed_value & self.int_mask
        for i in range(1, self.n):
            gross = self.state[i-1] ^ (self.state[i-1] >> 30)
            self.state[i] = (self.f * gross + i) & self.int_mask

        """ 

                Generator initialized with seed value. This implementation introduces
            a random 32-bit seed converted to an integer. A fixed seed is also
            okay if you need to debug or whatever.

                Ensure that the seed value fits within 32-bit range using 
            a bitwise AND operation.

            Result is stored in the first element of the state array self.state[0].

                Then we compute successive elements of self.state given the seed value. We
            iterate from 1 to the length of the self.state, computer variable 'gross'
            as the XOR of the previous state value shifted right 30 bits. Then compute 
            the new state value using the predefined constant f, and store it at self.state[i].
            That way, subsequent elements of the array are based on the previous state value.

        """


    def get_num(self) -> int:
        if self.index >= self.n:
            if self.index > self.n:
                raise MersenneError("Generator not seeded")
            self.twister()
        
        y = self.state[self.index]
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= y >> self.l

        self.index += 1
        return y & self.int_mask


    def twister(self) -> None:
        for i in range(self.n):
            x = (self.state[i] & self.upper_mask) + (self.state[(i + 1) % self.n] & self.lower_mask)
            xA = x >> 1
            if x & 1:
                xA ^= self.a
            self.state[i] = self.state[(i + 1) % self.n] ^ xA
        self.index = 0


if __name__ == '__main__':
    r = MersenneTwister()
    r.seed(int.from_bytes(urandom(4)))
    print("Sample values with random seed: ")

    for i, _ in enumerate(range(10), 1):
        print(f"Random number #{i} --> {r.get_num()}")

"""

        I'm seeding from 32 random bits in this implementation, though that's not necessary
    in the description of the challenge. I just wanted to ensure that different seeds would 
    generate different numbers. If you're looking to debug the program in closer detail,
    I'd recommend seeding with a fixed value, i.e. a constant seed of zero. 

        Jones. D. (2010). "Good Practice in (Pseudo) Random Number Generators for Bioinformatics
    Applications" gives decent tips for using RNGs well, including avenues for seeding. 
    In practice, a timestamp is an acceptable (and simple) way of seeding a generator with an 
    adequately large value, but can be hurtful if you're seeding multiple programs at the same
    time, i.e. one thousand simulation that depend on the RNG to induce randomness being seeded
    at the same time could result in less-than-adequate randomness in the simulations themselves. 
    
        Jones notes that /dev/urandom, which utilizes hardware timings to produce entropy, is a good 
    source, so I decided to use that in my program. 

"""



