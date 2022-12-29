
import socket
import time
URL='fun-with-flags.csa-challenge.com'
PORT = 6666

con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
con.connect((URL,PORT))
res = con.recv(1024).decode()
while 1:
    res =''
    con.send(f'2\n'.encode())
    while res =='':
        res = con.recv(1024).decode()
    #print(res)
    res =''
    con.send(f'20\n'.encode())
    while res == '':
        res = con.recv(1024).decode()
    #print(res)
    for _ in range(20):
        res =''
        con.send(f'15\n'.encode())
        while res == '':
            res = con.recv(1024).decode()
        print(res)
        if 'Failed to log' not in res:
            break
        print(res)
