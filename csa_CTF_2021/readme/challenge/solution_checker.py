from Crypto.Cipher import ARC4
import string
def check_key(key, key_checker_data):
    """ returns True is the key is correct.
        Usage:
        check_key('{I_think_this_is_the_key}', key_checker_data)
    """
    return ARC4.new(("CSA" + key).encode()).decrypt(key_checker_data) == b'success'


cp=open('key_checker_data','rb').read()

with open('./readme','r') as f:
    text = f.read().split()


clean_text =[]
for length in range(10):
    for w in text:
        clean_text.append(w.strip('\'":,(_}){-.?'))
    for i in range(len(text)-length):
        key = '{'+'_'.join(clean_text[i:i+length])+'}'
        try:
            print('trying: {}'.format(key))
            if check_key(key,cp):
                print('found the key!')
                print('CSA{}'.format(key))
                exit(0)
                
        except:
            continue
print("Key not found..")