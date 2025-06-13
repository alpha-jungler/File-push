"""def tri_recursion(K):
    if(K>0):
        result=K + tri_recursion(K-1)
        print(result)
    else:
        result=0
    return result
print("Recursion Results:")
tri_recursion(20)"""

import numpy as np
pq= np.read_csv('rikesh.csv')
print(pq.to_string())