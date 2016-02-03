#!/bin/env python2
#author: mp
#comment: factorials of sys.argv[1]
import sys

n = 1
f = 1
while n <= int( sys.argv[1] ):
    f = n * f
    n += 1
print f
