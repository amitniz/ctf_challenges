import sys
import re

file =''
try:
    with open(sys.argv[1],'r') as f:
        file = f.read()
except:
    print('[!] No Input File..')

#Extract the encyrpted values from the file.
bits = [chr(int(i,16)) for i in re.findall('0x[\S]{2}',file)]


#Switch function
def switchBits(char,p1,p2):
    mask1 = 1<<p1
    mask2 = 1<<p2
    bit1 = ord(char) & mask1
    bit2 = ord(char) & mask2
    rest = ord(char) & ~(mask1 | mask2)
    shift = p2-p1
    result = chr((bit1<<shift) | (bit2>>shift) | rest)
    return result

for i in range(len(bits)):
    c = bits[i]
    c = switchBits(c,6,7)
    c = switchBits(c,2,5)
    c = switchBits(c,3,4)
    c = switchBits(c,0,1)
    c = switchBits(c,4,7)
    c = switchBits(c,5,6)
    c = switchBits(c,0,3)
    c = switchBits(c,1,2)
    bits[i] = c

#Output
print('picoCTF{'+''.join(bits)+'}')



