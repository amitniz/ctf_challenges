
img1 = []
img2 = []
img3 = []
flag = ''

with open('mystery.png','rb') as img_bytes:
    img1 = list(img_bytes.read())
with open('mystery2.png','rb') as img_bytes:
    img2 = list(img_bytes.read())
with open('mystery3.png','rb') as img_bytes:
    img3 = list(img_bytes.read())

flag+=(chr(img2[-2]-21))
flag+=(chr(img3[-8]))
flag+=(chr(img3[-7]))
flag+=(chr(img2[-1]-4))
flag+=(chr(img1[-16]))
flag+=(chr(img3[-6]))
for i in range(-15,-11):
    flag+=(chr(img1[i]))
for i in range(-5,0):
    flag+=(chr(img3[i]))
for i in range(-11,-1):
    flag+=(chr(img1[i]))

print(flag)
