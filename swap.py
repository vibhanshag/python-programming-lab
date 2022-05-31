a=int(input('Enter 1st value: '))
b=int(input('Enter 2nd value: '))
print('Values before swapping are a=',a,' b=',b)
a=a^b
b=a^b
a=a^b
print('Values after swapping are a=',a,' b=',b)
