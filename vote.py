def vote(age):
	return a>=18
	
	
a=int(input("enter age of person"))
out=vote(a)
print(out)


#if to find name in dictionary

info={'ravi':12,'raj':45,'naman':18}
out={k: v for k,v in info.items}
