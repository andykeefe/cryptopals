![default](https://github.com/andykeefe/andykeefe/assets/154836099/26dfbd98-e0fd-4acc-9f95-049a97328683)

_Ciphers and Constellations in Love with a Woman_ by Joan Miró, 1941


## Block and Stream Cryptography

More block ciphers! Aren't you overjoyed?

This set focuses a bit more on CTR mode, which uses a block cipher as a stream cipher. The block cipher takes in a unique counter value each time, for example, an increasing counter as a new block is computed, and an initialization vector that stays the same. It is important to avoid using the same counter more than once. Therefore, CTR mode is theoretically very secure but relies on precise implementation. 

![image](https://github.com/andykeefe/andykeefe/assets/154836099/27c50f8b-8262-4d62-b69a-19a897cb8f66)


The last four exercises of this set revolve around the MT19937 Mersenne Twister Pseudo-Random Number Generator (PRNG), based on Mersenne prime $`2^{19937} - 1`$, including implementation, cracking the seed, cloning from output, creating a stream cipher from it and breaking it. It's quite mathematical, but Matsumoto and Nishimura (1998) gives good information about why this generator exceeded others in terms of performance, and how it can be used in a cryptographically secure system. Note that the MT19937 PRNG is not cryptographically secure in itself but needs to have its output converted with a secure hash algorithm [1].

![image](https://github.com/andykeefe/andykeefe/assets/154836099/33c6e730-f57d-4afa-86db-75143511e27a)


A random number generator intends to randomly generate sequences from an initial seed value. The goal is to approximate a sequence of random looking numbers even though the function itself is deterministic. Cryptographically secure pseudo-random number generators (CSPRNGs) are supposed to be unpredictiable and are unique to cryptographic applications, especially stream ciphers [2]. 

## References

[1] Matsumoto, M., & Nishimura, T. (1998). "Mersenne twister: A 623-Dimensionally Equidistributed Uniform Pseudo-Random Number Generator." ACM Transactions on Modeling and Computer Simulation, 8(1). p. 7

[2] Paar, C., & Pelzl, J. (2010). _Understanding Cryptography_. pp. 35-36.

## Exercises

1. The CBC padding oracle
2. Implement CTR, the stream cipher mode
3. Break fixed-nonce CTR mode using substitutions
4. Break fixed-nonce CTR statistically
5. Implement the MT19937 Mersenne Twister RNG
6. Crack an MT19937 seed
7. Clone an MT19937 RNG from its output
8. Create the MT19937 stream cipher and break it

