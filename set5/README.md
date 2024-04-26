![Ulam_spiral,Prime_factors_spiral](https://github.com/andykeefe/andykeefe/assets/154836099/53478f87-74a5-4ad6-a3ee-274c9235940f)

_Ulam Spiral_ by Stanisław Ulam, 1964


# Number Theoretic Cryptography


The last four sets have dealt with symmetric cryptography, for example, block ciphers like AES, and MACs using symmetric keys. Symmetric cryptography has been the standard for thousands of years. Now we're getting into the newer, far more mathematical field of asymmetric cryptography, or public key cryptography. Public key algorithms rely on three types of computational problems:

1. Integer factorization: RSA is based on this, for example
2. Discrete logarithms in finite fields: Diffie-Hellman is based on this, for example
3. Elliptic curve schemes: Elliptic Curve Diffie Hellman (ECDH) is based on this, for example 

## Interger factorization and RSA

First, I'll talk about integer factorization. I'll assume that you know what a prime number is. You can google it if you don't. An interesting mathematical principle is that every number can be factored into a unique set of primes. This is the Fundamental Theorem of Arithmetic, first described in Euclid's _Elements_, stated by Kamal al-Din al-Fārisī, and formally proved by Gauss. 

Take these examples:

- $`54 = 3\times 3\times 3 \times 2 `$


- $`165 = 11 \times\ 3 \times\ 5 `$


- $`654,654,681 = 3 \times\ 3 \times\ 23 \times\ 47 \times\ 67289 `$


- $`4,654,879,854,656 = 2 \times\ 2 \times\ 2 \times\ 2 \times\ 2 \times\ 2 \times\ 5153 \times\ 14114593`$

Think about the increasing complexity of these examples; the larger the number, the more difficult it becomes to factor into unique primes. This is one of the core security principles of RSA, formalized in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman (but actually discovered a few years earlier by researchers at Britain's GCHQ), which is one of the algorithms covered in the latter half of this set. RSA will generate a product of two primes, a semi-prime $` n = pq `$, that is over 600 digits long; factoring this integer is currently too intensive to be computationally feasible. Advances in quantum computing may change this in the future, but for now, quantum decoherence and costly quantum error-correction makes efficient cryptanalysis impractical for quantum computers.

RSA wasn't the birth of asymmetric/public-key cryptography. That would come a year earlier, in 1976, by Whitfield Diffie and Martin Hellman. Just kidding, the GCHQ, specifically James H. Ellis, formulated the concept of public key cryptography in 1969 but it was classified until 1997, after he died [1]. GCHQ was cooking, apparently. 

## Diffie-Hellman and the Discrete Logarithm Problem

Anyway. Before getting into the discrete logarithm problem, let's look at how Diffie-Hellman key exchange is set up and operates. 

- First, choose a large prime _p_.
- Choose an integer α ∈ {2, 3, ..., _p_ - 2}.
- Publish _p_ and α

![image](https://github.com/andykeefe/andykeefe/assets/154836099/f21ea42e-8324-4df2-9483-eac5c0b601a0)

_k_ is the shared secret that will act as the session key between the two parties doing the key exchange.
Here's a better look at the sequence with which the key is exchanged [2]:

![image](https://github.com/andykeefe/andykeefe/assets/154836099/eaa49610-d4d7-4c11-a7e4-9952248e7ad9)


To fully understand the discrete logarithm problem, it helps to have some background in abstract algebra, which I'm sure sounds really fun for you. I'll give some resources below for those willing to satiate their curiosity and fulfill their understanding as robustly as possible.

If you've studied calculus and some linear algebra, check out this free textbook:
- Beezer, R.A. (2015). _A First Course in Linear Algebra_.
  - Part 1 (pp. 11-74)

If you want a quick mathematical overview:
- Hoffstein, J., et al. (2008). _An Introduction to Mathematical Cryptography_.
  - pp. 72-75

If you want a quicker overview:
- Paar, C., Pelzl, J. (2010). _Understanding Cryptography_.
  - pp. 208-219

### Set theory, group theory, and modular arithmetic

Let's first discuss basic set theory and groups starting with modular arithmetic. Instead of trying to do a long winded mathematical explanation, I'll just use an example. Imagine a set $`Z^*_n `$ where _n_ = 15. The set consists of all integers _i_ where in $`gcd(i, n) = 1 `$, meaning all integers that are relatively prime to _n_. In this case, the set is {1, 2, 4, 7, 8, 11, 13, 14}. Here is the multiplication table for $` Z^*_{15} `$:

![image](https://github.com/andykeefe/andykeefe/assets/154836099/72830ea5-713a-40fd-a311-4a84554b3152)

For example, take the numbers in the set 7 and 8. Multiply them and you get 56. $` 56 mod 15 = 11 `$. You take the remainder of whole number multiplications on 15 to find the answer. 15 can go into 56 three times without exceeding 56. $` 15 \times\ 3 = 45 `$ but $`15 \times\ 4 = 60 `$. The remainder of the operation $` 15 \times\ 3 `$ is 11. 

Notice that the group is closed; any of the numbers in our set are also contained in the table, and no numbers outside of the set are in the table. There are other conditions that need to be met, but that's a basic primer on modular arithmetic. 

### Cyclic groups

Cyclic groups are the basis for discrete-logarithm cryptography schemes (Paar and Pelzl, 2010, p. 211). You can determine the _order_ of an element _a_ in a group $`Z^*_n`$ by determining the smallest integer _k_ such that:
$`a^k = a \circ\ a \circ\ a \circ\  ...  \circ\ a = 1`$ Let's look at an example.

Using our previous group $` Z^*_{15} `$, let's choose an element of it to find its order. Recall that the set of elements in the group is {1, 2, 4, 7, 8, 11, 13, 14}. In this example, we'll find _ord_(_7_):
- $` a^1 = 7 `$
- $`a^2 = 49 `$ **mod** $` 15 = 4 `$
- $`a^3 = 343  `$ **mod** $` 15 = 13 `$
- $` a^4 = 2401 `$ **mod** $` 15 = 1 `$

So the order of the element 7 is 4, $` ord(7) = 4 `$.

We can check if $` Z^*_{15} `$ is a _cyclic group_. A cyclic group contains an element, called a _primative element_, that generates every other element within the group, and therefore has a maximum order. Let's try to find a primitive element in $` Z^*_{15} `$:

I know that 2 and 4 are not primitive elements because both will quickly end up with remainder 1, and we know 7 is not a primitive element because we already found it's order. Lets try _a = 8_.

- $` a^1 = 8 `$
- $` a^2 = 64 `$ **mod** $` 15 = 4 `$
- $` a^3 = 512 `$ **mod** $` 15 = 2 `$
- $`a^4 = 4096 `$  **mod** $` 15 = 1 `$

8 is not a primitive element of $` Z^*_{15} `$ because $`ord(8) = 4`$. 

11 is not a primitive element either, so let's try _a = 13_:
- $`a^1 = 13 `$
- $`a^2 =  `$ **mod** $` 15 = 4 `$
- $` a^3 = 2197 `$ **mod** $` 15 = 7 `$
- $` a^4 = 64 `$ **mod** $` 15 = 4 `$  
-  $`a^5 = 28561 `$ **mod** $` 15 = 1 `$

13 is not a primitive element of $` Z^*_{15} `$ because  $`ord(13) = 4`$. Let's try _a = 14_.

- $` a^1 = 14 `$
- $`a^2 = 196 `$ **mod** $` 15 = 1 `$

14 is not a primitive element of $` Z^*_{15} `$ because $` ord(14) = 2 `$. There are no primitive elements in the group $` Z^*_{15} `$ so it is not a cyclic group. 

Let's look at another group $` Z^*_{10} `$ to find a primitive element. Remember, the set contains all elements less than 10 that are relatively prime to 10, meaning they share no common divisors. In this case the set is {1, 3, 7, 9}. Let _a = 3_ to find out if it's a primitive element or generator.

- $`a^1 = 3 `$ 
- $`a^2 = 9 `$
- $`a^3 = 27 `$ **mod** $` 10 = 7 `$
- $`a^4 = 81 `$ **mod** $` 10 = 1 `$

We see that _a = 3_ is a primitive element of the group $` Z^*_{10} `$ because it generates every element of the set, so _ord_(3) = _4_. Therefore we can conclude that $` Z^*_{10} `$ is a cyclic group.

There are also subgroups, but I don't feel like writing about them.

## References

[1] Hoffstein, J., Pipher, J., Silverman, J. (2008). _An Introduction to Mathematical Cryptography_. p. 59.

[2] Paar, C., & Pelzl, J. (2010). _Understanding Cryptography_. pp. 206-207.


Set 5 Problems
------------------------------------------
1. Implement Diffie-Hellman
2. Implement a MITM key-fixing attack on Diffie-Hellman with parameter injection
3. Implement DH with negotiated groups, and break with malicious "g" parameters
4. Implement Secure Remote Password (SRP)
5. Break SRP with a zero key
6. Offline dictionary attack on simplified SRP
7. Implement RSA
8. Implement an E=3 RSA Broadcast attack
