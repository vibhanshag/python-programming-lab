n=int(input("Enter Number of Lines to read: "))
f=open("sample.txt","r")
for i in range(n):
	data=f.readline()
	print(data)
f.close()
