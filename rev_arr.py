import numpy as np
ls=list(map(float,input().split()))
ar = np.array(ls)
res = ar[::-1]
print("final array", str(res))
