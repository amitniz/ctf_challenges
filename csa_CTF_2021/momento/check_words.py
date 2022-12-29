import enchant
import string
#pos = [3, 3, 6, 8, 9, 8, 6, 3, 3, 3, 2, 6, 2, 7, 7, 7, 4, 7, 8, 9, 2]
pos = [ 8,8,9]
#_ at 6
d = enchant.Dict("en_US")
#d.check(word)
pos_dic ={}
for c in string.ascii_lowercase:
    if (ord(c)%9 +1) not in pos_dic.keys():
        pos_dic[ord(c)%9 +1] = c
    else:
        pos_dic[ord(c)%9 +1]+=c
print(pos_dic)
def check_words(pos_dic,pos,i,word):
    if i == len(pos):
        #print(f'trying: {word}')
        if d.check(word):
            print(word)
        return

    for c in pos_dic[pos[i]]:
        try_word = word[:i] +c 
        check_words(pos_dic,pos,i+1,try_word)

check_words(pos_dic,pos,0,'')    
    
