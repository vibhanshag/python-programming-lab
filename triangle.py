a=int(input('Enter 1st side: '))
b=int(input('Enter 2nd side: '))
c=int(input('Enter 3rd side: '))
if (a+b<c or a+c<b or b+c<a):
	print('Inavlid triagnle')
elif (a==b & a==c & b==c):
	print('Triangle is equilateral')
elif ( a*a==(b*b)+(c*c) or b*b==(a*a)+(c*c) or c*c==(b*b)+(a*a)):
	print('Trianlge is right angled')
elif (a==b or a==c or b==c):
	print('Triangle is isoscles')
elif (a!=b & a!=c & b!=c):
	print('Triangle is scalene')
else:
	print('wrong input')
