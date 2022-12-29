import requests
from randcrack import RandCrack

PRINTABLE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+-/:.;<=>?@[]^_`{}"
URL ='http://slot-machine-reloaded.csa-challenge.com/'

FLAG_LEN = 32
flag_table = [list(PRINTABLE) for i in range(FLAG_LEN)]
flag= [' ' for i in range(FLAG_LEN)]
def get_random_string(session_id):
    return requests.get(URL+'spin/?coins=0',headers={'Cookie':session_id}).json()['result']


def extractRandomValue(string):
    binary_values = []
    for c in string:
        binary_values.append(format(PRINTABLE.index(c),'#0%db' %8)[2:])
    
    decimal_values =[]
    binary_192 = ''.join(binary_values)
    
    for i in range(0,len(binary_192),32):
        decimal_values.append(int(binary_192[i:i+32],2))
    return decimal_values[::-1]  #backward because I found out that that's how python creates the 192b number.

def extract_letters(predict,result_string):
    res =[]
    converted =format(predict,'#0%db' %194)[2:]
    for i in range(32):
        if int(converted[6*i:6*i+6],2) == 0:
            res.append((result_string[i],True))
        else:
            res.append((result_string[i],False))
    return res


res = requests.get(URL)
session_id = res.headers['Set-Cookie'].split(';')[0]

machine_rand= 0
rc = RandCrack()
for _ in range(200):
    random_string = get_random_string(session_id)
    print(f'\r[{["-","|","/"][ _ %3]}] Collecting generated numbers: | {random_string} | ',end='')

    if machine_rand> 575: #the submit method needs exactly 624 32bit gererated numbers so: 200*6-624=576
        last_randoms=[]
        last_randoms = extractRandomValue(random_string)    
        for n in last_randoms:
            #submit only the last 624 for better accuracy
            rc.submit(n)
    else:
        machine_rand+=6
print(f'\r[+] Collecting generated numbers: ',end='')
print('\n[+] Done.')



#Now the fun part..
print("[+] Ok, let's guess some numbers..")
while flag.count(" "):
    random_string = get_random_string(session_id)
    predicted = rc.predict_randrange(0, (2**192)-1)
    positions = extract_letters(predicted,random_string)

    for i,pos in enumerate(positions):
        if len(flag_table[i])>1 and pos[1]:
            flag_table[i] = pos[0]
            flag[i]= pos[0]
        else:
            if len(flag_table[i]) > 1 and pos[0] in flag_table[i] :
                flag_table[i].remove(pos[0])


    for i in range(FLAG_LEN):
        if len(flag_table[i]) == 1:
            flag[i] = flag_table[i][0]
    print(f'\r[+] status: {"".join(flag)} ',end='')

print(f'\r[*] Flag: {"".join([c[0] for c in flag])}  \n')