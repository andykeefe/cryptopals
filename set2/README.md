![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/6dfaab0f-5988-4563-a4e1-f86161f31ee8)


_Perspectival Drawing with Three Cubes_ by Peter Flötner, 1528


# Block Cipher Cryptography

This section covers cryptography most commonly used in the web: block ciphers. Block ciphers encrypt each block of plaintext with the same key. The length of the block depends on the cipher. For example, AES uses 128 bit length blocks, while DES uses 64 bit length blocks. 

Block ciphers are excellent for providing diffusion. On average, one change in plaintext bit results in the change of half of the output bits [1]. 

![image](https://github.com/andykeefe/andykeefe/assets/154836099/0c8d1475-36f8-4915-8121-9de7d2fb5569)

Block ciphers can be used in some hash functions. For example, the Davies-Meyer hash constructions use block cipher techniques. _e_ represents a block cipher in the expression below.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/5c5097d0-defb-411a-ac74-aa32f22d187e)

### Modes

The exercises in this set revolve mainly around ECB and CBC modes of encryption. ECB is weaker than CBC. ECB is highly deterministic; identical plaintext blocks result in identical ciphertext blocks. The classic example of this uses an image of Tux, the Linux mascot, and encrypts it in ECB mode. In Shannon's terms, this encryption mode is weak when it comes to diffusion; the statistical properties of the plaintext are not adequately obscured in the ciphertext.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/4ac81e17-b078-493f-b094-3cc15ce13d05)

CBC mode is safer. The encryption of a the first block includes an initialization vector (IV) that is XORed with the plaintext block. All subsequent plaintext block are XORed with the previously encrypted block, and so on. So the first ciphered block depends on the plaintext and IV; the second ciphered block depends on the second plaintext, the first ciphered block, and the IV. The third ciphered block depends on the third plaintext, the second and first ciphered block, and the IV, and so on.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/a0796044-f6cc-40c1-b043-7f03fcbe42b7)

Challenge 10 has us decrypt a text in CBC mode. 

![Untitled drawing](https://github.com/andykeefe/cryptopals/assets/154836099/d01a25c7-b068-4b5a-9220-372ee90f7279)


### Padding and PKCS #7

Some block cipher modes like ECB and Cipher Feedback mode require the length of the plaintext to be an exact multiple of the block size for the cipher used; in these cases, we may need to add padding to the plaintext [2]. For example, assume that $`P `$ is our plaintext, $` L(P) `$ is the byte-length of the plaintext, and $` b `$ is the block size in bytes of the cipher used. 

We determine the number of padding bytes _n_ such that $` n + L(P) \equiv 0 (\text{mod} \space {b})`$, meaning the plaintext with padding must be a multiple of the block size. Additionally, the value of each byte appended is dictated by the number of padding bytes. So if you need to pad with 4 bytes, as in the case of challenge 9 in this set (Implement PKCS#7 padding), the appended bytes will be b'/x04/x04/x04/x04'. If you only needed to pad with 2 bytes, the appended bytes would be b'/x02/x02'. This is the theory behind PKCS #7 [3]. 

PKCS #7 is one of the most popular padding schemes, according the the Cryptopals authors. 

## References

[1] Paar, C., & Pelzl, J. (2010). _Understanding Cryptography_. p. 58.

[2] Paar and Pelzl. (2010). p. 124.

[3] RFC 5652: Cryptographic Message Syntax (CMS). (2009). IETF Datatracker. https://datatracker.ietf.org/doc/html/rfc5652#section-6.3

## Exercises for set 2

1. Implement PKCS#7 padding
2. Implement CBC mode
3. An ECB/CBC detection oracle
4. Byte-at-a-time ECB decryption (Simple)
5. ECB cut-and-paste
6. Byte-at-a-time ECB decryption (Harder)
7. PKCS#7 padding validation
8. CBC bitflipping attacks

------------------

I've run into a bit of a challenge for this set. My cryptopals exercises are categorized by which ever set they're in. I have a directory /cryptopals that has subdirectories for each set, /set1, /set2, etc. 

Because of this, I'm unable to typically import functions from previous exercises like I was able to do in set one, simply using from <module> import <function>. I'm exploring workarounds, and once I have access to my machine again I will try to change the PYTHONPATH environment variable to include the cryptopals directory. This should allow me to import functions from set1 to be used in set2 exercises. 
