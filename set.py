#!/usr/bin/env python2

lengths = [ 1.0 ]
newlengths = []
removed_sum = 0.0
count = 0
while True:
    newlengths = []
    for length in lengths:
        third = length * 0.33
        removed_sum += third
        newlengths.append( third )
        newlengths.append( third )
    lengths = newlengths
    print "[>] Removed length: {}".format( str( removed_sum ) )
    if removed_sum > 1.0:
        break
    count += 1
print "[+] After {} cycles the removed length is greater than the initial line length".format( str( count ) )
