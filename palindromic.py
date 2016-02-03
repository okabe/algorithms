#!/bin/env python2
#author: mp
#comment: check if sys.argv[1] is a palindromic number
#         https://en.wikipedia.org/wiki/Palindromic_number
import sys

n = int( sys.argv[1] )
t = int( sys.argv[1][::-1] )
if n % t == 0:
    print "{} is palindromic".format( str( n ) )
else:
    print "{} is not palindromic".format( str( n ) )
