str1 = raw_input('Input string here : ')
str2 = raw_input('Input key here : ')

ans = []

#n=strlen(str1);

n=len(str1)

i = 0

print "Encrypted string : "

while i<n:
#    temp=unichr(ord(str1[i])^ord(str2[i]))#ord to change unit string to integer(unicode) and unichar for the reverse
   
    temp=str(ord(str1[i])^ord(str2[i]))   
   
    ans.append(temp.zfill(3))
   
    i=i+1
    
    #print temp,#prints with a space

    #print str(temp).zfill(3).join("")
    
print "".join(ans)#blank output
