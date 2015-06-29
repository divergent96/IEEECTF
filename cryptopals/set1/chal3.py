import sys
from mymodules import *
import operator
import numpy as np
from collections import Counter

msg = sys.argv[1].decode('hex')

similarityarr = dict()

for key in xrange(0,256):
    sample = xorstr(msg,chr(key))
    similarityarr[key] = similarity(charfreq.values(),frequency(sample).values())

best = max(similarityarr.iteritems(),key = operator.itemgetter(1))[0]#Seems this function uses operator.itemgetter(1) fetches the value from the array at key row and column 1 and feeds it to iteritems which is used in max 
#For more reference see link http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

print best
print xorstr(msg,chr(best))
