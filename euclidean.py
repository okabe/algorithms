#!/usr/bin/env python2
#author: mp
#comment: find the greatest common divisor of sys.argv[1] and sys.argv[2]
#         https://en.wikipedia.org/wiki/Euclidean_algorithm

import sys

n1 = int( sys.argv[1] )
n2 = int( sys.argv[2] )
r  = 0

while True:
    m = n1 % n2
    if m != 0:
        r = m
    else:
        print "GCD = {}".format( str( r ) )
        break
    n1 = n2
    n2 = r
