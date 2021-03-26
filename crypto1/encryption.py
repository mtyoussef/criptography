#Encryption
msg = input()
key = int(input())
list=[]
for i in msg :
    x = ord(i) + key
    if x>122 :
        x = x - 26
        ch = chr(x)
        list.append(ch)
    else :
        ch = chr(x)
        list.append(ch)
print("".join(list))
