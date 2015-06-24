from sys import argv
import base64

script , hexstring = argv

out = base64.b64encode(hexstring.decode('hex'))

print "The String in base64 is :"+ out
