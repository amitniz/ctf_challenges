import json
import requests
import copy
import hashlib
import random
from ast import literal_eval
import time
URL = "https://puzzword.csa-challenge.com/"
N_X = 7
N_Y = 7
UP='^'
DOWN='v'
RIGHT='>'
LEFT='<'
directions =[UP,DOWN,LEFT,RIGHT]
MAX_TIME = 0.8
TIMES =80

def print_board(board):
    for r in board:
        print r
    

def create_board(in_board):
    #creates board with 'x' where is nothing
    out_board =[]
    length_y = len(in_board)
    length_x = 0
    for j in range(length_y):
        length_x =max(length_x,len(in_board[j].strip()))
    for i in range(length_y):
        formatted = str(in_board[i]).strip().center(length_x,'x')
        out_board.append(list(formatted))
    return length_x,length_y,out_board

def count_board(board):
    count=0

    for i in range(N_Y):
        for j in range(N_X):
            if board[i][j] =='O':
                count+=1

    return count

def check_num(board,dst_board):
    return count_board(board) >= count_board(dst_board)

def can_move(x,y,direction,board):
    if direction == UP:
        if y > 1 and board[y][x] =='O' and board[y-1][x] =='O' and board[y-2][x] == '.':
            return True
    elif direction == DOWN:
        if y < N_Y-2 and board[y][x] =='O' and board[y+1][x] =='O' and board[y+2][x] == '.':
            return True
    elif direction == LEFT:
        if x > 1 and board[y][x] =='O' and board[y][x-1] =='O' and board[y][x-2] == '.':
            return True
    elif direction == RIGHT:
        if x < N_X-2 and board[y][x] =='O' and board[y][x+1] =='O' and board[y][x+2] == '.':
            return True
    else:
        assert(0)

    return False

#return the move to append and update the board
def move(x,y,direction,board):
    #return the move to append and update the board
    new_board = copy.deepcopy(board)
    if direction == UP:
        new_board[y][x] ='.'
        new_board[y-1][x]='.'
        new_board[y-2][x]='O'
        return [x,y,UP],new_board
    elif direction == DOWN:
        new_board[y][x] ='.'
        new_board[y+1][x]='.'
        new_board[y+2][x]='O'
        return [x,y,DOWN],new_board
    elif direction == LEFT:
        new_board[y][x] ='.'
        new_board[y][x-1]='.'
        new_board[y][x-2]='O'
        return [x,y,LEFT],new_board

    elif direction == RIGHT:
        new_board[y][x] ='.'
        new_board[y][x+1]='.'
        new_board[y][x+2]='O'
        return [x,y,RIGHT],new_board
    else:
        assert(0)
 
def solve(steps,board,solution,init_time,order):
    if board == solution:
        return 1,steps

    if time.time()-init_time > MAX_TIME:
        return -1,steps

    if not check_num(board,solution):
        return 0,steps
    for pos in order:
        for direction in directions: 
            if can_move(pos[0],pos[1],direction,board):
                step,new_board = move(pos[0],pos[1],direction,board)
                steps.append(step)
                #print_board(new_board)
                res,steps = solve(steps,new_board,solution,init_time,order)
                if res ==1:
                    return 1,steps
                elif res ==-1:
                    return -1,steps
                else:
                    steps.pop()

    return 0,steps


res =requests.get(URL+"puzzle").json()

stage=1
import sys
if  len(sys.argv) ==2 and sys.argv[1] == 'last' :
    with open('solutions','r') as f:
        solutions = f.read().split('\n') 
        
    last_level = {"puzzle_id":solutions[-6],"solution":literal_eval(solutions[-4])}
    res =requests.post(URL+"solve",data=json.dumps(last_level)).json()
    print str(res)
    stage = solutions[-2]
#try:
while 1:
    #Get Data
    puzzle_id = json.loads(res["message"])["puzzle_id"]
    src_board = json.loads(res["message"])["source_board"]
    dst_board = json.loads(res["message"])["destination_board"]
    N_X,N_Y,src_board = create_board(src_board)
    N_X,N_Y,dst_board = create_board(dst_board)
    
    print 'Now Solving:'
    print_board(src_board)
    print '-----------------'
    print_board(dst_board)
    
    #Check cache
    steps = None
    hashed = hashlib.md5(str(src_board)+str(dst_board)).hexdigest()
    print hashed
    with open('solutions','r') as f:
        solutions = f.read().split('\n')
        if hashed in solutions:
            solution =solutions[solutions.index(hashed)+1]
            print "I know that one"
            steps = literal_eval(solution)

    if steps is None:
        print 'start solving stage {}'.format(stage)
        #Solve
        order =[]
        for i in range(N_Y):
            for j in range(N_X):
                order.append((j,i))
        times=0
        while times <TIMES:
            #s,steps = random_solve([],src_board,time.time(),order)
            s,steps =solve([],src_board,dst_board,time.time(),order)
            if s==1:
                break
            random.shuffle(order)
            times+=1
            print 'stage {}: try again..'.format(stage)
        if s==1:
            with open('solutions','a+') as f:
                solved_stages =f.read().split()
                f.write(puzzle_id+'\n')
                f.write(hashed+'\n')
                f.write(str(steps)+'\n')
                f.write('stage:{}\n----------------------\n'.format(stage))
            print 'solved'
        
        #  if s==-1:
        #     order =[]
        #    for i in range(N_Y):
            #       for j in range(N_X):
            #          order.append((j,i))
            #   print "everyday i'm shuffling"
            # random.shuffle(order)
            # init_time =time.time()
            # s,steps = random_solve(steps,src_board,init_time,order)
        

        if s ==-1:
            print 'reset!'
            stage =1
            #MAX_TIME=5
            res =requests.get(URL+"puzzle").json()
            continue
    stage+=1

    solution = {"puzzle_id":puzzle_id,"solution":steps}
    res = requests.post(URL+"solve",data=json.dumps(solution)).json()
    print str(res)
    with open('responses.txt','a') as f:
        f.write('stage {}:\n'.format(stage))
        f.write(hashed+'\n')
        f.write(str(res)+'\n')
    
    #MAX_TIME+=2*stage

#except Exception as e:
#    print 'something went wrong..'

