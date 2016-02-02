#!/usr/bin/env python2
#author: mp
#comment: just a fun math trick, i doubt this will ever be useful. take any number greater then 9
#         add digits together, subtract the sum from the original number, add the digits of the
#         result together and it will always -eq 9

import sys

n = int( sys.argv[1] )

def add( n ):
    s = 0
    for i in list( str( n ) ):
        s += int( i )
    return s

def algo( n ):
    f = 0
    s = add( n )
    d = n - s
    for j in list( str( d ) ):
        f += int( j )
    return f

r = algo( n )

while True:
    if len( list( str( r ) ) ) is not 1:
        r = add( r )
    if r is 9:
        print "told you so"
        break
