![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/b4e27e08-8ad6-48d0-ab82-a90deae91386)

Building a Catafalque, Tomb of Ipuy, 1279 BCE-1213 BCE

# Basics, XOR operations, and symmetric cryptography


The authors call this a qualifying set. It gets you ready to write and think like a cryptographer. It requires a level of knowledge beyond just introductory coding, and it's definitely necessary to have open documentation for Python while doing it.

This set covers XOR operations and introduces the most widely used symmetric cryptographic scheme, the Advanced Encryption Standard (AES). We'll start by introducing the concepts behind symmetric cryptography, including its history and conventional operations, and then we'll briefly cover what the XOR operation does to bits. 

## Symmetric cryptography

Cryptography has been around for thousands of years. The first documented, surviving example of cryptography comes from Ancient Egypt, 1900 BCE, but didn't seem to be used for secretive communication as much as to glorify the death of a noblemen. One of the most well-known and widely used examples of historical cryptographic communication comes from Julius Caesar [1]. You may know him from his crossing of the Rubicon or that time he got stabbed a bunch of times. The cipher he used (appropriately referred to as a 'Caesar Cipher') used a numerical value to shift and substitute the plaintext message. For example, assume our plaintext message is "ITHINKIWILLCONQUERGAUL" and our key is 3. Each letter would then be shifted and substituted by the letter 3 characters from it. 'I' becomes 'L', 'T' becomes 'W', 'H' becomes 'K', and so on. So our original message 

ITHINKIWILLCONQUERGAUL

is encrypted to

LWKLQNLZLOOFRQTXHUJDXO

To decrypt the ciphered message, the recipient would need to have knowledge of the key. The encryption and decryption key are of the same value, just with "reversed" operations. This is the concept of _symmetric keys_, and the backbone of today's symmetric cryptography: to decrypt an encrypted message, both parties **must** share the same key.

It's true that _every_ historical cipher used symmetric keys; for nearly 3000 years, symmetric key cryptography was the only way to go [2]. Mathematical breakthroughs in the 1960s and 1970s introduced public-key cryptography, or asymmetric cryptography, where in each party has a public key and private key, but we'll talk more about this in another set. Now we'll move on to briefly explaining the XOR operation. 

## XOR operations

Exclusive-or, referred to as XOR, is a bitwise operation, meaning it operates on ones and zeros. Rooted in the earlier 20th century, the XOR operation was used in a _one time pad_, where the key is the length of the message. This was wildly inefficient, and new methods of encryption were sought.

In an XOR operation, a set of ones and zeros is added to another set of ones and zeros. The result of the operation is considered 0 if the XORed values are the same, and 1 if the two values are different. For example if you XOR 1101 with 0111, you get 1010. If 1111 is XORed with 0000, the result is 1111. If 0001 is XORed with 1011, the result is 1000 [3].

## Advanced Encryption Standard (AES)

The Rijndael algorithm was developed in the late 1990s. In 2001 it was officially designated as the Advanced Encryption Standard by the NIST after several rounds of competition among different algorithms. 

AES is the most commonly used symmetric algorithm used today. It is considered very secure, even garnering the label of quantum-resistant if it is implemented properly. AES is designed to operate on 128-bit input blocks, and can use either 128-bit, 192-bit, or 256-bit keys. If you were trying to do an exhaustive key space search or a brute force of AES-128, it would take you more than 10,000,000,000,000,000,000,000 years [4]. That's much, much longer than the age of the universe. 

This set implements and attacks AES in ECB mode. There's more info on ECB mode in the next set write-up, but for now it should be noted that ECB is not considered secure because of its failure to adequately obscure the statistical properties of the plaintext. 

---------------------------------------------------------------------------------------------

### References

[1] Sidhpurwala, H. (2023, January 12). A Brief History of Cryptography. Red Hat Blog. https://www.redhat.com/en/blog/brief-history-cryptography 

[2] Smart, N. (2008). _Cryptography: An Introduction_. p. 35.

[3] Dunin, E., & Schmeh, K. (2023). _Codebreaking: A Practical Guide_. p. 398.

[4] Boneh, D., Shoup, V. (2023). _A Graduate Course in Applied Cryptography_. p. 114-117. 

# Exercises for set 1

1. Convert hex to base64
2. Fixed XOR
3. Single-byte XOR cipher
4. Detect single character XOR
5. Implementing repeating key XOR
6. Break repeating key XOR
7. AES in ECB mode
8. Detect AES in ECB mode
