import sys
import re


file=''
try:
    with open(sys.argv[1],'r') as f:
        file =f.read()
except:
    print('[!] Missing file location argument..')
nums = [bin(int(i))[2:] for i in re.findall('== (\d*)',file)]
nums = [(32-len(i))*'0'+i for i in nums] #fix to 32bit   

out = []

for n in nums:
    for i in range(0,32,8):
        out.append(chr(int(n[i:i+8],2)))

print('picoCTF{'+''.join(out)+'}')
