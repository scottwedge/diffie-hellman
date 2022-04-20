#!/usr/bin/env python3

# Computation examples for Diffie-Hellman key exchange

# from: https://brilliant.org/wiki/diffie-hellman-protocol/

#Description of the Algorithm

#Together Alice and Bob choose a large prime number 'p' and a number 'g' such that 1<g<p. (Usually 'g' is chosen to be quite small, for ease of computation.) These numbers do not need to be secret, so they can be communicated freely over a public channel. Alice secretly chooses an integer 'n' and Bob secretly chooses an integer 'm'.

#Now Alice sends Bob the number g**n(mod p), and Bob sends Alice g**m(mod p). 

#Using her secret 'n' Alice computes s= (g**m)**n mod p. Using his secret 'm' Bob computes s= (g**n)**m mod p. Now Alice and Bob have a secret key 's' known only to them, which can be used to send messages via any number of secure private-key cryptosystems.

# Example:    Let p=191 and g=2. Suppose Alice picks 42 and Bob picks 33.Then Alice computes 2**42 mod 191 = 20 and Bob computes 2**33 mod 191 =103. They send the results of these computations to each other. Upon receiving 103, Alice computes 103**42 mode 191 = 115, and Bob computes 20**33 mod 191 = 115. So they have a key that they have agreed on without disclosing their secret numbers to each other. They can use this key to communicate securely via a cryptosystem of their choosing. 

# Imports
import random

# Functions
def create_prime_list(a, b):
    primes_list = []  # Init list
    # Create list of primes between a and b
    if type(a) is not int  or type(b) is not int:
        print("Both {} and {} need to be integers.".format(a,b))
    else:
        for j in range(a, b+1, 1):
#            print("Testing____ ",j)  #DEBUG
            for num in range(2, j):
                if j % num == 0:   # Not a prime number if divisible
#                    print("j={} not prime since divisible by num={}".format(j, num))  #DEBUG
                    break
                if num == j-1:
#                    print("   Testing____ {} never == 0".format(j))  #DEBUG
                    primes_list.append(j)  # Add to list of prime numbers
#                    print(j)  # To display progress to user  #DEBUG
    return primes_list


def random_prime(l):
    # Choose a random prime number from list
    index = random.randint(0, len(l) - 1)
    return l[index]


def random_small_number(min, max):
    # Return a small number between min and max for value 'g'
    g = random.randint(min, max)
    return g

def random_secret_number(min, max):
    # Return a number between min and max for secret 'n' or 'm'
    g = random.randint(min, max)
    return g


def a_to_b_mod_c(a, b, c):
    result = a ** b % c
    return result

def show_all_calculations():
    prime_list = create_prime_list(151, 191)
    #print("List of primes is: {}.".format(prime_list))
    
    p = random_prime(prime_list)
    print("Random prime value= {}    from list {} (for modulo calculation).".format(p, prime_list))
    
    g = random_small_number(2,4)
    print("Random small number (used as base of exponentiation) for both users is: {}.".format(g))
    
    n = random_small_number(30, 50)
    print("Random small number 'n' (used as exponent) for user N is: {}.".format(n))
    
    m = random_small_number(30, 50)
    print("Random small number 'm' (used as exponent) for user M is: {}.".format(m))
    
    g_to_n_mod_p = a_to_b_mod_c(g, n, p)
    print("User N calculates g to the n ({}) mod p ({}) (send value to M) value= {}.".format(g**n, p, g_to_n_mod_p))
    
    g_to_m_mod_p = a_to_b_mod_c(g, m, p)
    print("User M calculates g to the m ({}) mod p ({}) (send value to N) value= {}.".format(g**m, p, g_to_m_mod_p))
    
    secret_M = a_to_b_mod_c(g_to_n_mod_p, m, p)
    print("Secret value for user M = {} calculated as {} ** {} mod {} = {} mod {}.".format(secret_M, g_to_n_mod_p, m, p, g_to_n_mod_p ** m, p))
    
    secret_N = a_to_b_mod_c(g_to_m_mod_p, n, p)
    print("Secret value for user N = {} calculated as {} ** {} mod {} = {} mod {}.".format(secret_N, g_to_m_mod_p, n, p, g_to_m_mod_p ** n, p))



if __name__ == "__main__":
    show_all_calculations()
