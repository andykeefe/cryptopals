![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/6dfaab0f-5988-4563-a4e1-f86161f31ee8)


_Perspectival Drawing with Three Cubes_ by Peter Flötner, 1528


## Block Cipher Cryptography

This section covers cryptography most commonly used in the web: block ciphers. Block ciphers encrypt each block of plaintext with the same key. The length of the block depends on the cipher. For example, AES uses 128 bit length blocks, while DES uses 64 bit length blocks. 

Block ciphers are excellent for providing diffusion. On average, one change in plaintext bit results in the change of half of the output bits [1]. 

![image](https://github.com/andykeefe/andykeefe/assets/154836099/0c8d1475-36f8-4915-8121-9de7d2fb5569)

Block ciphers can be used in some hash functions. For example, the Davies-Meyer hash constructions use block cipher techniques. _e_ represents a block cipher in the expression below.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/5c5097d0-defb-411a-ac74-aa32f22d187e)

The exercises in this set revolve mainly around ECB and CBC modes of encryption. ECB is weaker than CBC. ECB is highly deterministic; identical plaintext blocks result in identical ciphertext blocks. The classic example of this uses an image of Tux, the Linux mascot, and encrypts it in ECB mode. In Shannon's terms, this encryption mode is weak when it comes to diffusion; the statistical properties of the plaintext are not adequately obscured in the ciphertext.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/4ac81e17-b078-493f-b094-3cc15ce13d05)

CBC mode is safer. The encryption of a the first block includes an initialization vector (IV) that is XORed with the plaintext block. All subsequent plaintext block are XORed with the previously encrypted block, and so on. So the first ciphertext depends on the plaintext and IV; the second ciphertext depends on the second plaintext, the first plaintext, and the IV. The third ciphertext depends on the third, second, and first plaintext and the IV, and so on.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/a0796044-f6cc-40c1-b043-7f03fcbe42b7)

## References

[1] Paar, C., & Pelzl, J. (2010)._Understanding Cryptography_. p. 58.


## Exercises for set 2


1. Implement PKCS#7 padding
2. Implement CBC mode
3. An ECB/CBC detection oracle
4. Byte-at-a-time ECB decryption (Simple)
5. ECB cut-and-paste
6. Byte-at-a-time ECB decryption (Harder)
7. PKCS#7 padding validation
8. CBC bitflipping attacks
