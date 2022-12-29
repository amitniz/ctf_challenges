


KEY = '\xcc\x55\xaa'
pt = input()
cp =''.join([chr(ord(pt[i])^ord(KEY[i %len(KEY)])) for i in range(len(pt))]) 
print(cp)
