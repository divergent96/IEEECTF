encrypted = "b4e3:6;:"
out = []
for i in xrange(0,len(encrypted)):
    out.append(chr(ord(encrypted[i])-i))
    
print "".join(out)
