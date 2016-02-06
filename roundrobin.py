#!/bin/env python2
#author: mp
#comment: delegate a set of items amongst a set of receivers where sys.argv[1]
#         is the number of items and sys.argv[2] the number of recievers.. I
#         called it round robin because im unaware of a formal name if there
#         is one

import sys

nitem = int( sys.argv[1] )
nrecv = int( sys.argv[2] )
recievers = []

class Reciever:
    """ just something to hold items """
    def __init__( self, ident ):
        self.ident = ident
        self.items = []

for i in range( 1, nrecv + 1 ): #add all recievers to array
    recievers.append( Reciever( i ) )

count  = 0
for i in range( 1, nitem + 1 ): #delegate item to reciever
    elem = count % len( recievers )
    recievers[elem].items.append( i )
    print "delegated {} to reciever {}".format( str( i ), str( elem ) )
    count += 1
