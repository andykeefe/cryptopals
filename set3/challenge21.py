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

            Generator initialized with seed value, in our case, 47.

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
    r.seed(0)
    print("Sample values (seed=0):")
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())
    print(r.get_num())

