#XOR's two strings and outputs their binary as integer
def strxorbin(str1,str2):
    c = []
    
    for i in range(0,len(str1)):
        c.append(int(bin(ord(str1[i]) ^ ord(str2[i]))[2:].zfill(8))) 

    return c
#end 1

#Length of Integer function
def intlen(num):
    if(num == 0):
        return 0;
    else:
        return 1+intlen(num/10)
#end 2   

#Fuction to find edit distance
def editdistance(str1,str2):
    
    editdistance = 0

    arr1 = strxorbin(str1,str2)

    for i in range(0,len(str1)):
        num1 = arr1[i]
        for j in range(0,intlen(num1)):
            num2 = num1%10
            if(num2 == 1):
                editdistance += 1;
            num1/=10;
         
    return editdistance
#end 3
#End of user functions               

str1 = "this is a test"
str2 = "wokka wokka!!!"
print editdistance(str1,str2)

