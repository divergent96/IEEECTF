import sys
from mymodules import *
import operator
import numpy as np
from collections import Counter

msg = sys.argv[1].decode('hex')

similarityarr = dict()

for key in xrange(0,256):
    sample = xorstr(msg,chr(key))
    similarityarr[key] = similarity(charfreq.values(),Counter(sample).values())
        
best = max(similarityarr.iteritems())

print xorstr(msg,chr(best))
