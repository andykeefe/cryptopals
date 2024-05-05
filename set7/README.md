![Château_d'Anet_-_Anet_-_Eure-et-Loir_-_France_-_Mérimée_PA00096955_(52)](https://github.com/andykeefe/cryptopals/assets/154836099/ac007f56-7131-4a58-be4d-d729f1cf0bed)

Philibert De l’Orme, 1553. _Dome of the chapel of château d’Anet_. [From Wikimedia user "Binche".](https://commons.wikimedia.org/wiki/File:Ch%C3%A2teau_d%27Anet_-_Anet_-_Eure-et-Loir_-_France_-_M%C3%A9rim%C3%A9e_PA00096955_(52).jpg)


# Hash Functions and Message Authentication Codes

This is the first area of the problems that deals with hashes. A cryptographic hash function is one-way; just like it is easier to smash a tea cup than to put that tea cup back together, a cryptographic hash function should be easy to do but difficult to reverse. This notion of _pre-image resistance_ is easy to illustrate. Imagine a hash function $`h`$ that takes an arbitrarily sized input $`x`$, and spits out a fixed length output $`y`$, the hash value. That is,

$`h(x) = y`$

Pre-image resistance means that given the output $`y`$, it should be computationally infeasible to compute the input value $`x`$. 

_Second pre-image resistance_ or _weak collision resistance_ means that given an input $`x_1`$, it should be very hard to find another input $`x_2`$ with same hash value. That is, 

$`h(x_1) = y = h(x_2) `$

Similarly, it should challenging to find any two inputs $`x`$ and $`x'`$ with the same hash value.

$`h(x) = h(x')`$

This is _collision resistance_, and is the most challenging property to meet when it comes to cryptographic hash functions [1].


### References

[1] Smart, N.P. (2013). _Cryptography: An Introduction_. pp. 153-154.

