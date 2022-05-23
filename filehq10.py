with open('sample.txt') as f:
	data=f.read()
	words=data.split()
	print(len(words))
