import binascii
import sys

str1 = raw_input("TEXT INPUT :")
str2 = raw_input("KEY :")

out = ''    
for i in xrange(0,len(str1)):
    out += chr(ord(str1[i])^ord(str2[i%len(str2)]))
    
print out.encode('hex')
    


