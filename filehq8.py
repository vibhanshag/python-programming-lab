with open('sample.txt') as f:
	data=f.read().split()
	re=max(data,key=len)
print(re)
