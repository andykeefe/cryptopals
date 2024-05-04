![default](https://github.com/andykeefe/cryptopals/assets/154836099/c224ad1a-94d1-4b12-9320-9d0c279e2924)

_A Camel_, 1646. Cornelis Saftleven.

## More Number Theoretic Cryptography

This section covers concepts related to RSA and the Digital Signature Algorithm, DSA. We briefly mentioned RSA in last set's write up in the context of integer factorization, but made no mention of DSA because while it relies on modular exponentiation and the discrete logarithm problem, it is gradually being phased out in favor of other digital signature schemes. Accordingly, FIPS 186-5 (2023) states the standard that DSA no longer be used for digital signature generation, but may be used for digital signature verification for signatures generated prior to the standard's date of implementation (2/03/2023). 

We'll now cover RSA and DSA in more detail. Warning: equations abound.

### RSA

The security of the RSA algorithm resides in the difficulty of solving equations in the form $` x^e \equiv c \pmod n `$. $` e `$, $` c `$ and $`n `$ are all known; only $`x `$ is unknown. Let's illustrate the RSA cryptoscheme using two parties, Alice and Bob. Alice and Bob want to establish communication with one another.

1. Alice will pursue _key generation_.
- First she chooses _secret primes_, $` p `$ and $` q `$
- Then she chooses an encryption exponent $` e `$ such that $` gcd(e, (p - 1)(q - 1) = 1 `$
- Finally, she publishes the semi-prime $`n = pq `$, being sure to discard $`p`$ and $`q`$, and $`e `$. Her public key is $`(N, e)`$

2. Bob will pursue _encryption_.
- First he chooses a plaintext message $` m `$
- Then he uses Alice's public key $`(N, e)`$ to compute $` c \equiv m^e \pmod N `$
- Finally, the ciphertext $` c `$ is sent to Alice.

3. Alice will pursue _decryption_.
- First she computes $`d`$, the decryption exponent, satisfying the following equation: $` ed \equiv 1 \pmod{ (p-1)(q-1)} `$
- Then she computes $` m' \equiv c^d \pmod N `$
- $`m' = m`$

The security of the scheme relies on the following:
- $`p`$ and $`q`$ are extremely large primes, and $` N = pq `$
- One who knows the values of $`p`$ and $`q`$ can easily solve for $`x`$ in the following equation: $` x^e \equiv c \pmod n `$
- One who does _not_ know the values of $`p`$ and $`q`$ cannot easily find $`x`$ due to the difficulty of _large integer factorization_ [1]


### References
[1] Hoffstein, J., Pipher, J., & Silverman, J. (2008). _An Introduction to Mathematical Cryptography_. p. 119.
