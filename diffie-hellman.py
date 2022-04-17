#!/usr/bin/env python3

# Computation examples for Diffie-Hellman key exchange

# from: https://brilliant.org/wiki/diffie-hellman-protocol/

#Description of the Algorithm

#Together Alice and Bob choose a large prime number 'p' and a number 'g' such that 1<g<p. (Usually 'g' is chosen to be quite small, for ease of computation.) These numbers do not need to be secret, so they can be communicated freely over a public channel. Alice secretly chooses an integer 'n' and Bob secretly chooses an integer 'm'.

#Now Alice sends Bob the number g**n(mod p), and Bob sends Alice g**m(mod p). 

#Using her secret 'n' Alice computes s= (g**m)**n mod p. Using his secret 'm' Bob computes s= (g**n)**m mod p. Now Alice and Bob have a secret key 's' known only to them, which can be used to send messages via any number of secure private-key cryptosystems.

# Example:    Let p=191 and g=2. Suppose Alice picks 42 and Bob picks 33.Then Alice computes 2**42 mod 191 = 20 and Bob computes 2**33 mod 191 =103. They send the results of these computations to each other. Upon receiving 103, Alice computes 103**42 mode 191 = 115, and Bob computes 20**33 mod 191 = 115. So they have a key that they have agreed on without disclosing their secret numbers to each other. They can use this key to communicate securely via a cryptosystem of their choosing. 


