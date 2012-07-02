import sys
import Prime_Tester

'''

MPN Check

This module should eliminate exponents by test it with Lucas-Lehmer primality test

In order to start operation one should send list of prime numbers

'''

if (len(sys.argv) < 2):
    raise NameError("oops, you didn't give 1 argument.")

list_size = int(sys.argv[1])
prime_list = [0] * list_size
pt = Prime_Tester.Prime_Tester()

for i in range(0, list_size):
    p = prime_list[i]
    if (pt.isMPN(p)):
        print("OMG!!! New MPN Found!!!\n\n")
        print("********************** The p number is: ")
        print(p)
        print(" **********************\n\n")
    

