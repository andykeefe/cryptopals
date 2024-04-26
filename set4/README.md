![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/3e402585-384e-4857-92a0-6e403ebb2a0b)

_Stamp Seal Inscribed for Amenhotep I_, New Kingdom, 1525-1504 BCE


Stream Cryptography and Randomness
------------------------------------------------

This set is the last focused on block cipher cryptography, and also covers message authentication codes. We've already covered block and stream ciphers, CTR and CBC mode, and a little about initialization vectors, so this write up will focus on authentication, MAC, and hashing algorithms.

Authentication is an easy concept to grasp. When you log into something, you need to enter a password or a biometric scan to verify that you are who you say are, when you use an ATM, you need to enter a PIN to access the account; when you try to trade a knock-off Babe Ruth baseball card from the 1930s, the auctioneer first verifies the authenticity (or lack, thereof) of the card. 

Message authentication codes (MACs) are one-way hash functions that provide integrity and authentication. Unlike other one-way functions, they are dependent on a key, specifically symmetric keys. Schneier notes the following: "An easy way to turn a one-way hash function into a MAC is to encrypt the hash value with a symmetric algorithm. Any MAC can be turned into a one-way hash function by making the key public" [1]. The following is a generic notation described by Paar and Pelzl (2010) to describe MACs, as well as a diagram showing the principles of MAC calculation and verification:

$`m = MAC_k(x) `$

where _m_ is the authentication tag, _k_ is a symmetric key, and _x_ is a message [2].

![image](https://github.com/andykeefe/andykeefe/assets/154836099/d43943a0-f3d4-4ce1-bde7-0bdf98320993)

## References

[1] Schneier, B. (2015). _Applied Cryptography, Second Edition_. pp. 455-456.

[2] Ibid, p. 320

Exercises
------------------------
1. Break "random access read/write" AES CTR
2. CTR bitflipping
3. Recover the key from CBC with IV=Key
4. Implement a SHA-1 keyed MAC
5. Break a SHA-1 keyed MAC using length extension
6. Break an MD4 keyed MAC using length extension
7. Implement and break HMAC-SHA1 with an artificial timing leak
8. Break HMAC-SHA1 with a slightly less artificial timing leak
