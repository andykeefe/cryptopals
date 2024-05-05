![Château_d'Anet_-_Anet_-_Eure-et-Loir_-_France_-_Mérimée_PA00096955_(52)](https://github.com/andykeefe/cryptopals/assets/154836099/830c753a-9d42-4bd3-907a-23c4d217d638)


Philibert De l’Orme, 1553. _Dome of the chapel of château d’Anet_. [From Wikimedia user "Binche".](https://commons.wikimedia.org/wiki/File:Ch%C3%A2teau_d%27Anet_-_Anet_-_Eure-et-Loir_-_France_-_M%C3%A9rim%C3%A9e_PA00096955_(52).jpg)


# Hash Functions and Message Authentication Codes

## Cryptographic hash functions

This is the first area of the problems that deals with hashes. A cryptographic hash function is one-way; just like it is easier to smash a tea cup than to put that tea cup back together, a cryptographic hash function should be easy to do but difficult to reverse. This notion of _pre-image resistance_ is easy to illustrate. Imagine a hash function $`h`$ that takes an arbitrarily sized input $`x`$, and spits out a fixed length output $`y`$, the hash value. That is,

$`h(x) = y`$

Pre-image resistance means that given the output $`y`$, it should be computationally infeasible to compute the input value $`x`$. 

_Second pre-image resistance_ or _weak collision resistance_ means that given an input $`x_1`$, it should be very hard to find another input $`x_2`$ with same hash value. That is, 

$`h(x_1) = y = h(x_2) `$

Similarly, it should challenging to find any two inputs $`x`$ and $`x'`$ with the same hash value.

$`h(x) = h(x')`$

This is _collision resistance_, and is the most challenging property to meet when it comes to cryptographic hash functions [1].

### Standardized hash functions today

FIPS 180-4 specifies several secure hash algorithms (SHA) to be used:  SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256 [2]. It should be noted that the use of SHA-1 has been deprecated since 2011, and there is a plan as of 2022 to transition away from its currently limited usage [3]. 

This set of cryptopals exercises contains one focused on the MD4 hash function (designed by Ron Rivest, one of the authors of the RSA algorithm). Security weaknesses in MD4 were first described in 1991, just a year after its introduction, and it has been illustrated to suffer from collision attacks. MD4 is therefore not a standardized hash algorithm, and should not be used in applications. This makes it a good exercise. 

## Message Authentication Codes

Schneier (2015) defines a message authentication code (MAC) as a "key-dependent one way hash function" [4]. The MAC is computed as a function of the message and a symmetric key. Paar and Pelzil (2010) use the following notation for MAC functions:

$` t = MAC_k(m)`$ where $`t`$ is the authentication tag, $`k`$ is the symmetric key, and $`m`$ is the message [5]. 

### CBC-MAC

We can construct a MAC using a block cipher by using the CBC-MAC technique. The message $`m`$ is split into blocks, and the first block is XORed with a block cipher $`E`$ using a secret key $`k`$ and produces an output. The second block is XORed with the output of the previous operation on the first block and put through the block cipher using the secret key and produces an output that will be used in the succeeding block, and so on. Here's an illustration:

![Untitled drawing (1)](https://github.com/andykeefe/cryptopals/assets/154836099/3aa00614-f4d9-4947-8030-6cdbd5223376)

A common block cipher used in CBC-MAC techniques is AES. It should be noted that CBC-MAC is not an NIST-approved authentication mode in and of itself because of "security deficiencies"[6], but does approve of it being used in Counter with Cipher Block Chaining-Message Authentication Code (CCM) technique [7].

### References

[1] Smart, N.P. (2013). _Cryptography: An Introduction_. pp. 153-154.

[2] National Institute of Standards and Technology. (2015) _Secure Hash Standard (SHS)_. FIPS PUB 180-4.

[3] National Institute of Standards and Technology. (2022). _NIST Transitioning Away from SHA-1 for All Applications_. https://csrc.nist.gov/news/2022/nist-transitioning-away-from-sha-1-for-all-apps

[4] Schneier, B. (2015). _Applied Cryptography_. p. 455. 

[5] Paar, C. and Pelzl, J. (2010). _Understanding Cryptography_. p. 320.

[6] National Institute of Standards and Technology. (2005). _Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication_. NIST SP 800-38B.

[7] National Institute of Standards and Technology. (2004). _Recommendation for Block Cipher Modes of Operation: The CCM Mode for Authentication and Confidentiality_. NIST SP 800-38C.
