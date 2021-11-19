n=int(input("Enter the number: "))
for i in range(1,n+1//2):
    if n==i*i:
        print("Perfect Square")
        break
else:
	print("Not perfect square")