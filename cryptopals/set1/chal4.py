#import enchant
import sys
import binascii

#checker = enchant.Dict("en-US")
#Making a word list from basic ubuntu dictionary for comparison
words = set()

with open('dict.txt','rb') as wordfile:
    for word in wordfile.read().split('\n'):
        words.add(word.upper())
#End 1

#Function returns if the text given is legible enough to be counted as english
def is_eng(text):
    ratio = 0.5
    word_count = 0
    word_alike = 0
    
    for word in text.split():
        word_alike +=1
        if word.upper() in words:
            word_count += 1
            
        if word_alike == 0 or word_count == 0:
            return False
            
        return float(word_count) / word_alike >= ratio
#End 2

#Making ciphertext list        

if __name__ == "__main__":
    with open('data4.txt','rb') as c_file:
        ciphers = list(line.rstrip() for line in c_file)
    
    for cipher in ciphers:
        cipherdata = cipher.decode('hex')
        for key in xrange(0,256):
            cleardata = ''
            for i in xrange(0,len(cipherdata)):
                data = ord(cipherdata[i]) ^ key 
                if data in xrange(32, 128) or data == 10 or data == 13: # only add printables to speed up later part
                    cleardata += chr(data)
                else:
                    break
                    
            if is_eng(cleardata.decode()) and (len(cleardata) == len(cipherdata)):
                print "%3d " % key, cipher, cleardata


