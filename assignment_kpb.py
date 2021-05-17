s=int(input("Shift value:"))
message=input("Message")


lower_alphabet="abcdefghijklmnopqrstuvwxyz"
upper_alphabet=lower_alphabet.upper()


def encrypt(x,m):
    msg=""
    for i in m:
        if(i == ' '):
            msg+=' '
            continue
        
        
        if(not i.isupper()):
            r=lower_alphabet.index(i)
            r=(r+x)%26
            msg+=lower_alphabet[r]
        else:
            r=upper_alphabet.index(i)
            r=(r+x)%26
            msg+=upper_alphabet[r]
    return msg

def decrypt(x,m):
    msg=""
    for i in m:
        if(i == ' '):
            msg+=' '
            continue
        
        
        if(not i.isupper()):
            r=lower_alphabet.index(i)
            r=(r-x)%26
            msg+=lower_alphabet[r]
        else:
            r=upper_alphabet.index(i)
            r=(r-x)%26
            msg+=upper_alphabet[r]
    return msg


msg=encrypt(s,message)
print(msg)

msg=decrypt(s,msg)
print(msg)
