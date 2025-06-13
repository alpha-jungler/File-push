"""def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result= 0
    return result
print("Recursion Example Results:")
tri_recursion(6)"""

"""import numpy as np

arr= np.array([1, 2, 3, 4, 5, 6])

print(arr)
print(type(arr))"""
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
import pandas as pd
mn= pd.read_csv('annual-enterprise-survey-2023-financial-year-provisional.csv')
print(mn.to_string())



