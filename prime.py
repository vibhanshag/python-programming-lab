def prime(a):
	count=0
	if a==1:
		return False
	for i in range(2,(a//2)+1):
		if a%i==0:
			return False
	return True
num=int(input("enter a number "))
print(prime(num))
