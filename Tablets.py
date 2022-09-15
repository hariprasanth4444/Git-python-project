n=int(input("Enter the nth day: "))
d=n*24
r=d//5
print(r)
c=0
for i in range(1,n+1):
    c+=24
    r=c%5
    c=r
if r==4:
    print(4)
else:
    print(5)