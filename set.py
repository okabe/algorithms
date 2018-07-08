#!/usr/bin/env python2

"""
example of Georg Cantors infinite set theory

if you have a single line segment, in this example starting at 0.0 and ending at 1.0
then if you remove the center 3rd of the line, you have 2 lines left 0.0 -> 0.33, and
0.66 -> 1.0. if you continue to remove the center third of every line left over in an
infinite loop, the total removed length of the line will exceed the original length of
the whole line. this shows that you can have different sizes of infinity.

careful, this script can exhaust your system memory
"""

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
