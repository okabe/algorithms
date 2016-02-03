#!/bin/env python2
#author: mp
#comment: simple primality test given sys.argv[1]

import sys

n = int( sys.argv[1] )
i = 5
isprime = True

#avoid dropping into loop
if n <= 1:
    print "{} is less than 1, not prime".format( str( n ) )
    isprime = False
elif n <= 3:
    print "{} is prime".format( str( n ) )
    isprime = False
elif n % 2 == 0 or n % 3 == 0:
    print "{} is divisible by 2, 3, not prime".format( str( n ) )
    isprime = False
else:
    while i <= ( n / 2 ):
        if n % i == 0:
            print "{} is divisible by {}, not prime".format( str( n ), str( i ) )
            isprime = False
            break
        i += 1

if isprime is True:
    print "{} is prime".format( str( n ) )
