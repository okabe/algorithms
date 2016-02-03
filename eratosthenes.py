#!/usr/bin/env python2
#author: mp
#comment: snag all prime numbers up to a max value set by sys.argv[1]
#         https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes 
import sys

n = int( sys.argv[1] )
ignore = []
for i in range( 2, n + 1 ):
    for j in range( 2, n + 1 / i ):
        if i * j <= n:
            ignore.append( ( i * j ) )
for i in range( 2, n + 1 ):
    if i not in ignore:
        print i
