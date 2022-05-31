def check(ar,n):
    for i in range(n-2):
        if abs(ar[i]-ar[i+1]) >= abs(ar[i+1]-ar[i+2]):
            return False
    return True


import math
n=int(input())
ls=list(map(int,input().split()))
out=check(ls,n)
print(out)
