![default](https://github.com/andykeefe/cryptopals/assets/154836099/c224ad1a-94d1-4b12-9320-9d0c279e2924)

_A Camel_, 1646. Cornelis Saftleven.

## More Number Theoretic Cryptography

This section covers concepts related to RSA and the Digital Signature Algorithm, DSA. We briefly mentioned RSA in last set's write up in the context of integer factorization, but made no mention of DSA because while it relies on modular exponentiation and the discrete logarithm problem, it is gradually being phased out in favor of other digital signature schemes. Accordingly, FIPS 186-5 (2023) states the standard that DSA no longer be used for digital signature generation, but may be used for digital signature verification for signatures generated prior to the standard's date of implementation (2/03/2023). 

We'll now cover RSA and DSA in more detail. Warning: equations abound.

### RSA

The security of the RSA algorithm resides in the difficulty of solving equations in the form $` x^e \equiv c \pmod n `$. $` e `$, $` c `$ and $`n `$ are all known; only $`x `$ is unknown. 
