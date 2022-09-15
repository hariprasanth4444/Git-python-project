n=int(input())
c=int(input())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
s,k=0,0
while True:
    #print(k+v[v.index(max(v))])
    if (k+v[v.index(max(v))])>c:
        print(s)
        break
    k+=v[v.index(max(v))]
    s+=w[v.index(max(v))]
    i=v.index(max(v))
    v.pop(i)
    w.pop(i)
