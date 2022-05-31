def powe(a1,b1):
	power=1
	for i in 'h'*b1:
		power=power*a1
	return power
a=int(input('enter base'))
b=int(input('enter power'))
out=powe(a,b)
print(out)
