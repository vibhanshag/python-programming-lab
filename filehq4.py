n=int(input('enter last n lines to read'))
with open('sample.txt') as f:
	print(list(f)[-n:])
