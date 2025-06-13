import numpy as np
arr=np.array([3, 4, 5, 6, 7, 8])
M=arr.copy()
arr[0]=99
print(arr)
print(M)
import numpy as np
arr=np.array([8, 9, 10, 11, 12])
Q=arr.view()
arr[0]=77
print(arr)
print(Q)