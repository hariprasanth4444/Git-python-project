n,m=map(int,input("Enter n and m values ").split())
l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a,c,d,b=0,0,n-1,n-1
for k in range(n//2):
    for i in range(c,b+1):
        print(l[a][i],end=" ")
    a+=1
    for i in range(a,b+1):
        print(l[i][b],end=" ")
    b-=1
    for i in range(b,c-1,-1):
        print(l[d][i],end=" ")
    d-=1
    for i in range(d,a-1,-1):
        print(l[i][c],end=" ")
    c+=1