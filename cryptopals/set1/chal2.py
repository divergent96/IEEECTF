from sys import argv

script,str1,str2 = argv

out = []

n=len(str1)
for i in range(0,n):
    out.append(hex(int(str1[i],base=16)^int(str2[i],base=16)))
for i in range(0,n):
    out[i]=out[i][2:]    

print "".join(out)
