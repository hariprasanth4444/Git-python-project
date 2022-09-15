s='0'
a=int(input())
b=int(input())
while a>1:
    for i in s:
        s2=""
        if i=='0':
            s2+="01"
        else:
            s2+="10"
        s=s2
    a-=1
print(s)
print(s[b-1])
