import sys
import Prime_Tester
import random

'''

PM1_S:

This module should find list of random prime number

In order to start operation one should send the size of list

'''

if (len(sys.argv) < 2):
    raise NameError("oops, you didn't give 1 argument.")

list_size = int(sys.argv[1])
prime_list = [0] * list_size
pt = Prime_Tester.Prime_Tester()

for i in range(0, list_size):
    p = int(random.getrandbits(32)) # Get 32-bit random number

    #While p already in list or it's not a prime number -> random another one
    while (p in prime_list or not pt.isPrime(p)):
        p = random.getrandbits(32)
        
    #Add the prime number to list    
    prime_list[i] = p

            
            
            
            
            
            
            
            
            
            
            
            