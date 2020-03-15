import sys
import re


file =''
with open(sys.argv[1],'r') as f:
    file =f.read()

ext_txt = re.findall("0x[\d,\w]{1,2}",file)
print(''.join([chr(int(i,16)^int('0x55',16)) for i in ext_txt[:-1]]))

