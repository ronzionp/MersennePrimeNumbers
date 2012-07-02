import math

'''

First method:
The Lucas-Lehmer primality test is simple. 
It states that for P > 2, 2^P-1 is prime if and only if Sp-2 is zero in this sequence: 
S0 = 4, Sn = (Sn-1^2 - 2) mod (2^P-1). 

For example, to prove 2^7 - 1 (127) is prime:

        S0 = 4
        S1 = (4 * 4 - 2) mod 127 = 14
        S2 = (14 * 14 - 2) mod 127 = 67
        S3 = (67 * 67 - 2) mod 127 = 42
        S4 = (42 * 42 - 2) mod 127 = 111
        S5 = (111 * 111 - 2) mod 127 = 0
        
        
Second method:
Simple calculation for prime number, run from 2 - sqrt of number and check if divisible


'''

class Prime_Tester(object):

    def isMPN(self, p):
        if (p > 2):
            # calculate Mersenne Number -> 2^p - 1
            MN = (2**p) - 1
            
            S = 4
            for i in range(1, p-1):
                S = ((S**2) - 2) % MN
                
            if (S == 0):
                return True
            
        return False
    
    def isPrime(self, p):
        if (p > 1):
            sqrt = int(math.sqrt(p)) + 1
            for i in range(2, sqrt):
                if (p % i == 0):
                    return False
            return True
        else:
            return False          
            