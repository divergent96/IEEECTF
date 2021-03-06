import numpy as np

#Character frequency comparison table
charfreq = dict()
for i in xrange(0,256):
    charfreq[i]=0
    
charfreq[ord('a')] = 7.52766
charfreq[ord('e')] = 7.0925
charfreq[ord('o')] = 5.17
charfreq[ord('r')] = 4.96032
charfreq[ord('i')] = 4.69732
charfreq[ord('s')] = 4.61079
charfreq[ord('n')] = 4.56899
charfreq[ord('1')] = 4.35053
charfreq[ord('t')] = 3.87388
charfreq[ord('l')] = 3.77728
charfreq[ord('2')] = 3.12312
charfreq[ord('m')] = 2.99913
charfreq[ord('d')] = 2.76401
charfreq[ord('0')] = 2.74381
charfreq[ord('c')] = 2.57276
charfreq[ord('p')] = 2.45578
charfreq[ord('3')] = 2.43339
charfreq[ord('h')] = 2.41319
charfreq[ord('b')] = 2.29145
charfreq[ord('u')] = 2.10191
charfreq[ord('k')] = 1.96828
charfreq[ord('4')] = 1.94265
charfreq[ord('5')] = 1.88577
charfreq[ord('g')] = 1.85331
charfreq[ord('9')] = 1.79558
charfreq[ord('6')] = 1.75647
charfreq[ord('8')] = 1.66225
charfreq[ord('7')] = 1.621
charfreq[ord('y')] = 1.52483
charfreq[ord('f')] = 1.2476
charfreq[ord('w')] = 1.24492
charfreq[ord('j')] = 0.836677
charfreq[ord('v')] = 0.833626
charfreq[ord('z')] = 0.632558
charfreq[ord('x')] = 0.573305
charfreq[ord('q')] = 0.346119
charfreq[ord('A')] = 0.130466
charfreq[ord('S')] = 0.108132
charfreq[ord('E')] = 0.0970865
charfreq[ord('R')] = 0.08476
charfreq[ord('B')] = 0.0806715
charfreq[ord('T')] = 0.0801223
charfreq[ord('M')] = 0.0782306
charfreq[ord('L')] = 0.0775594
charfreq[ord('N')] = 0.0748134
charfreq[ord('P')] = 0.073715
charfreq[ord('O')] = 0.0729217
charfreq[ord('I')] = 0.070908
charfreq[ord('D')] = 0.0698096
charfreq[ord('C')] = 0.0660872
charfreq[ord('H')] = 0.0544319
charfreq[ord('G')] = 0.0497332
charfreq[ord('K')] = 0.0460719
charfreq[ord('F')] = 0.0417393
charfreq[ord('J')] = 0.0363083
charfreq[ord('U')] = 0.0350268
charfreq[ord('W')] = 0.0320367
charfreq[ord('.')] = 0.0316706
charfreq[ord('!')] = 0.0306942
charfreq[ord('Y')] = 0.0255073
charfreq[ord('*')] = 0.0241648
charfreq[ord('@')] = 0.0238597
charfreq[ord('V')] = 0.0235546
charfreq[ord('-')] = 0.0197712
charfreq[ord('Z')] = 0.0170252
charfreq[ord('Q')] = 0.0147064
charfreq[ord('X')] = 0.0142182
charfreq[ord('_')] = 0.0122655
charfreq[ord('$')] = 0.00970255
charfreq[ord('#')] = 0.00854313
charfreq[ord(',')] = 0.00323418
charfreq[ord('/')] = 0.00311214
charfreq[ord('+')] = 0.00231885
charfreq[ord('?')] = 0.00207476
charfreq[ord(';')] = 0.00207476
charfreq[ord('^')] = 0.00195272
charfreq[ord(' ')] = 0.00189169
charfreq[ord('%')] = 0.00170863
charfreq[ord('~')] = 0.00152556
charfreq[ord('=')] = 0.00140351
charfreq[ord('&')] = 0.00134249
charfreq[ord('`')] = 0.00115942
charfreq[ord('\\')] = 0.00115942
charfreq[ord(')')] = 0.00115942
charfreq[ord(']')] = 0.0010984
charfreq[ord('[')] = 0.0010984
charfreq[ord(':')] = 0.000549201
charfreq[ord('<')] = 0.000427156
charfreq[ord('(')] = 0.000427156
charfreq[ord('>')] = 0.000183067
charfreq[ord('"')] = 0.000183067
charfreq[ord('|')] = 0.000122045
charfreq[ord('{')] = 0.000122045
charfreq[ord('\'')] = 0.000122045
#End 1
#XOR's two given strings provided they are in string and not hex
def xorstr(msg,key):
    out = []
    for i in xrange(0,len(msg)):
        out.append(chr(ord(msg[i])^ord(key[i%len(key)])))
        
    out = "".join(out)
    return out
#End 2

#Calculates cosine similarity between two arrays.Used to compare text with frequency of letters.
def similarity(v1, v2):
    return (np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2))))
    
#End 3

def frequency(text):
    freq = dict()
    
    for i in xrange(0,256):
            freq[i]=0
    
    for char in text:
        freq[ord(char)] = text.count(char)
        
    length = len(text)
    
    #normalising the no of chars to a ratio to compare with preset freq's
    for x in freq:
        if length > 0:
            freq[x] = (float(freq[x])/length)*100.0
        else:
            freq[x] = float(0)
            
    return freq
