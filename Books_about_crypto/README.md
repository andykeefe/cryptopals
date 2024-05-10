![800px-Aeneas_cipher_disc,_5th_century_BC,_Greece_(reconstruction)](https://github.com/andykeefe/cryptopals/assets/154836099/8c771027-0203-4925-81fe-c297b8803e61)

_Aeneas Tacticus cipher disc_, 5th century BC. Thessaloniki Technology Museum.


# Cryptography Books

Throughout the blurbs I write for each set of problems, I often make reference to various texts. This section has a nearly complete list of texts referenced, or texts that I think are useful in understanding the topics but aren't explicitly stated. Think of it as a quick bibliography to tap into if you want to go deeper into these topics.

There are a few cases where a book I've referenced is not in this list; in that case, just search for the book on the Internet if you wish to know more.

Lastly, the vast majority of these books are very "academic." They're laborious to get through, and even tougher to understand if you're background on mathematics and computer science is minimal. Believe me, for I am you. For this reason, I'll include more "pop" cryptography books for the general reader, and I'll go further to annotate why I think these books are just as useful for the lay person in terms of getting an understanding of cryptography. Most should be available through your library or through an inter-library loan.

### General cryptography

- Boneh, D., Shoup, V. (2023). _A Graduate Course in Applied Cryptography_.
  - [_A Graduate Course in Applied Cryptography_](https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_6.pdf)  (free)

- Bray, S.W. (2020). _Implementing Cryptography Using Python_.
  - [_Implementing Cryptography Using Python_](https://www.wiley.com/en-ca/Implementing+Cryptography+Using+Python-p-9781119612209)
 
- Ferguson, N., Schneier, B., & Kohno, T. (2010). _Cryptography Engineering: Design Principles and Practical Applications._
  - [_Cryptography Engineering_](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118722367)
 
- McKay, D.J.C. (2003). _Information Theory, Inference, and Learning Algorithms_.
  - [_Information Theory, Inference, and learning Algorithms_](https://www.amazon.com/Information-Theory-Inference-Learning-Algorithms/dp/0521642981)

- Paar, C., Palzl, J. (2010). _Understanding Cryptography_.
  - [_Understanding Cryptography_](https://link.springer.com/book/10.1007/978-3-642-04101-3)

- Schneier, B. (2015). _Applied Cryptography, Second Edition_.
  - [_Applied Cryptography_](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119183471) ("find" online)

- Smart, N. (2008). Cryptography: An Introduction.
  - [_Cryptography: An Introduction_](https://www.cs.umd.edu/~waa/414-F11/IntroToCrypto.pdf) (free)

### Symmetric cryptography

- Boura, C., & Naya-Plasencia, M. (2024). _Symmetric Cryptography, Volume 1: Design and Security Proofs_.
  - [_Symmetric Cryptography, Volume 1_](https://onlinelibrary.wiley.com/doi/book/10.1002/9781394256358)

 
- Boura, C., & Naya-Plasencia, M. (2024). _Symmetric Cryptography, Volume 2: Cryptanalysis and Future Directions_.
  - [_Symmertric Cryptography Volume 2_](https://onlinelibrary.wiley.com/doi/book/10.1002/9781394256327)


- Cid, C., Murphy, S., & Robshaw, M. (2006). _Algebraic Aspects of the Advanced Encryption Standard_.
  - [_Algebraic Aspects of the Advanced Encryption Standard_](https://link.springer.com/book/10.1007/978-0-387-36842-9)


- Daemen, J., & Rijmen, V. (2002). _The Design of Rjindael: The Advanced Encryption Standard_.
  - [_The Design of Rjindael: The Advanced Encryption Standard_](https://link.springer.com/book/10.1007/978-3-662-60769-5)


- Sakiyama, K., Sasaki, Y., & Li, Y. (2016). _Security of Block Ciphers: From Algorithm Design to Hardware Implementation_.
  - [_Security of Block Ciphers_](https://www.wiley.com/en-us/Security+of+Block+Ciphers%3A+From+Algorithm+Design+to+Hardware+Implementation-p-9781118660010)


### Asymmetric cryptography

- Hoffstein, J., Pipher, J., Silverman J.H. (2008). _An Introduction to Mathematical Cryptography_.
  - [_An Introduction to Mathematical Cryptography_](https://link.springer.com/book/10.1007/978-0-387-77993-5)

- Pointcheval, D. (2022). _Asymmetric Cryptography: Primitives and Protocols._
  - [_Asymmetric Cryptography_](https://onlinelibrary.wiley.com/doi/book/10.1002/9781394188369)
 

### "Pop" cryptography

- Dunin, E., Schmeh, K. (2023) _Codebraking: A Practical Guide_.
  - [_Codebreaking: A Practical Guide_](https://nostarch.com/codebreaking)
  - Mostly deals with "classical" cryptography, the kind of stuff that was done through history like Caesar ciphers and Vigenere ciphers, the kind of stuff that was done by hand. Maybe not useful for today's highly esoteric algorithms, but still a great book for appreciating the history of cryptography and the rigors of classical cryptanalysis.
 
- Martin, K. (2020). _Cryptography: The Key to Digital Security, How it Works, and Why It Matters_.
  - [_Cryptography: The Key to Digital Security..._](https://wwnorton.com/books/9780393867459)
  - No math in this book, but does an excellent job at plainly explaining a _huge_ range of cryptographic concepts like bits and bytes, what a key is, how a block cipher works, popular algorithms, and a bunch of other stuff. Good book for a qualitative overview of a heavily quantitative field. 
 
- Singh, S. (1999). _The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography_.
  - [_The Code Book_](https://www.penguinrandomhouse.com/books/168002/the-code-book-by-simon-singh/)
  - Bit of an older book here, but still useful for explaining the history of cryptography. No mentions of AES, it didn't exist yet, but does go quite a bit into public-key algorithms and RSA. One of the most crucial points is that cryptanalysis is always getting better, and there is no guarantee that the algorithms of today will not be vulnerable in 5, 10, 20 years. I haven't picked this book up in awhile but I know it mentions post-quantum cryptography a bit.
