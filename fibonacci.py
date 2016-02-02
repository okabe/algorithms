#!/bin/env python2
#author: mp
#comment: all numbers in fibonacci sequence less than sys.argv[1]

import sys

f  = 0
f1 = 0
f2 = 1

while f <= int( sys.argv[1] ):
    print f
    f  = f1 + f2
    f1 = f2
    f2 = f
