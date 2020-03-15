import sys
import re
import base64

file =''
with open(sys.argv[1],'r') as f:
    file =f.read()

extracted_txt = re.findall('"J\w*"',file)
decoded_txt = ''.join([base64.b64decode(i).decode('utf-8') for i in extracted_txt])
print(''.join([chr(int(i,16)) for i in decoded_txt.split('%')[1:]]))

