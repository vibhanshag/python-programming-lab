import numpy as np
r,c=list(map(int,input().split()))
m1=[]
m2=[]
for i in range(r):
    ele=list(map(int,input().split()))
    m1.append(ele)
for i in range(r):
    ele=list(map(int,input().split()))
    m2.append(ele)
m1=np.array(m1)
m2=np.array(m2)
print('Addition:\n',np.add(m1,m2))
print('Subract\n',np.subtract(m1,m2))
print(np.multiply(m1,m2))
print(np.floor_divide(m1,m2))
print(np.med(m1,m2))
print(np.power(m1,m2))
