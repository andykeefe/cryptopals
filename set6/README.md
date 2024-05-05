![default](https://github.com/andykeefe/cryptopals/assets/154836099/c224ad1a-94d1-4b12-9320-9d0c279e2924)

_A Camel_, 1646. Cornelis Saftleven.

## More Number Theoretic Cryptography: RSA, DSA, and nonces

This section covers concepts related to RSA and the Digital Signature Algorithm, DSA. We briefly mentioned RSA in last set's write up in the context of integer factorization, but made no mention of DSA because while it relies on modular exponentiation and the discrete logarithm problem, it is gradually being phased out in favor of other digital signature schemes. Accordingly, FIPS 186-5 (2023) states the standard that DSA no longer be used for digital signature generation, but may be used for digital signature verification for signatures generated prior to the standard's date of implementation (2/03/2023). 

We'll now cover RSA and DSA in more detail. Warning: equations abound.

### RSA

_**Encryption and Decryption with RSA**_

The security of the RSA algorithm resides in the difficulty of solving equations in the form $` x^e \equiv c \pmod n `$. $` e `$, $` c `$ and $`n `$ are all known; only $`x `$ is unknown. Let's illustrate the RSA cryptoscheme using two parties, Alice and Bob. Alice and Bob want to establish communication with one another.

1. Alice will pursue _key generation_.
- First she chooses _secret primes_, $` p `$ and $` q `$
- Then she chooses an _encryption exponent_ $` e `$ such that $` gcd(e, (p - 1)(q - 1) = 1 `$
- Finally, she publishes the semi-prime $`N = pq `$, being sure to discard $`p`$ and $`q`$, and $`e `$. Her public key is $`(N, e)`$

2. Bob will pursue _encryption_.
- First he chooses a plaintext message $` m `$
- Then he uses Alice's public key $`(N, e)`$ to compute $` c \equiv m^e \pmod N `$
- Finally, the ciphertext $` c `$ is sent to Alice.

3. Alice will pursue _decryption_.
- First she computes $`d`$, the _decryption exponent_, satisfying the following equation: $` ed \equiv 1 \pmod{ (p-1)(q-1)} `$
- Then she computes $` m' \equiv c^d \pmod N `$
- $`m' = m`$

The security of the scheme relies on the following:
- $`p`$ and $`q`$ are extremely large primes, and $` N = pq `$
- One who knows the values of $`p`$ and $`q`$ can easily solve for $`x`$ in the following equation: $` x^e \equiv c \pmod N `$
- One who does _not_ know the values of $`p`$ and $`q`$ cannot easily find $`x`$ due to the difficulty of _large integer factorization_ [1].

_**Digital Signatures with RSA**_

The digital signature scheme with RSA is quite similar to the RSA encryption scheme. We'll use an example to illustrate their similarities. Patti is receiving a signed document by Andy, but she wants to validate the authenticity of the document and of Andy's identity.

1. Andy pursues _key generation_.
- Andy chooses secret primes $`p`$ and $`q`$
- Then he chooses a _verification exponent_ $`v`$ such that $`gcd(v, (p-1)(q-1)) = 1 `$
- Finally he publishes $` N = pq `$ and $`v`$

2. Andy pursues _signing_ of the document
- First he computes $`s`$ such that $` sv \equiv 1 \pmod{(p-1)(q-1)}`$
- Then he signs the document by computing $` S \equiv D^s \pmod n `$

3. Patti pursues _verification_ of the document
- She computes $` S^v \mod N `$ and checks that it is equal to $`D`$

You can see that the digital signature scheme for RSA has about the same set up as an RSA encryption scheme [2].

### Digital Signature Algorithm (DSA)

DSA was originally constrained to key length between 512 and 1024 bits; the key length has increased in accordance with improved cryptanalysis, but let's assume that 1024-bit is the standard. DSA involves two cyclic groups. The large cyclic group $`Z^*_p`$, derived from a 1024-bit prime, has an order of 1024 bits in length and is the main computational space for generating signatures, and a smaller subgroup $` Z^*_p `$ is determined by a prime $`q`$ with a typical bit length of 160 bits. These values will yield a signature with 320 bit length.

Now we'll look at the key generation, signature generation, and signature verification schemes for DSA with bit length 1024.

1. Key generation
- Generate prime $`p`$ such that $` 2^{1023} < p < 2^{1024} `$
- Generate prime divisor $`q`$ of $` p - 1 `$ such that $` 2^{159} < q < 2^{160} `$
- Find an element $`\alpha `$ such that $`\alpha`$ generates subgroup with $`q`$ elements, meaning $`ord(\alpha) = q`$
- Choose random integer $`d`$ such that $` 0 < d < q `$
- Compute $`\beta \equiv \alpha ^d \mod p`$
- Public key $`k_{pub} = (p, q, \alpha, \beta)`$
- Private key $`k_{pr} = (d) `$

2. Signature generation
- Choose integer as random ephemeral key $`k_E`$ such that $` 0 < k_E < q`$
- Calculate $` r \equiv (\alpha^{k_e} \mod p) \mod q`$
- Calculate $` s \equiv (SHA(x) + dr)k_e^{-1} \mod q`$, where, in this case, $`SHA`$ is the SHA-1 hash algorithm

3. Signature verification
- Calculate auxillary value $` w \equiv s^{-1} \mod q`$
- Calculate auxillary value $`u_1 \equiv w \cdot SHA(x) \mod q`$
- Calculate auxillary value $` u_2 \equiv w \cdot r \mod q`$
- Calculate $` v \equiv (\alpha^{u_1} \beta^{u_2} \mod p)\mod q `$
- Verification $`ver_{k_{pub}}(x(r, s))`$ is result of:
  - $`v \equiv r \mod q \implies `$ valid signature, signature accepted
  - $` v \not\equiv r \mod q \implies`$ invalid signature, message or signature were modified or sender had wrong public key
 
An attack on DSA could target the private key $`d`$, wherein the attacker tries to solve the discrete logarithm in the large cyclic group module $`p`$: 
    
  - $` d \equiv log_{\alpha} \beta \mod p`$

It's also important that the ephemeral key $`k_E`$ is never reused, so for every signing operation, a new randomly chosen ephemeral key is necessary [3].

### Nonces

A "nonce" is more than just funny British slang for sex offenders. Cryptographically speaking, a nonce, which may also be referred to as an initialization vector (IV), is a "**n**umber used **once**." The theory behind a nonce/IV is that it is a randomly generated or counter value that is unique to each use of the encryption scheme such that a duplicate plaintext message put through the encryption scheme results in a distinct ciphertext, even if the key is the same. The nonce need not be secret, but it must change each time the encryption scheme is used [4][5].



### References
[1] Hoffstein, J., Pipher, J., & Silverman, J. (2008). _An Introduction to Mathematical Cryptography_. p. 119.

[2] Hoffstein, et al. (2008). p. 441.

[3] Paar, C., Pelzl, J. (2010). _Understanding Cryptography_. pp. 277-282.

[4] Boura, C., & Naya-Plasencia, M. (2024). _Symmetric Cryptography, Volume 1: Design and Security Proofs_. p. 74

[5] Paar and Pelzl. 2010. p. 48.
