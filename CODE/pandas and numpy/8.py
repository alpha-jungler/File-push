import pandas as pd 
import numpy as np
p=pd.read_csv('rikesh.csv')
data_pandas=p.head(10)
data_numpy=data_pandas.to_numpy()
print("first 10 rows from pandas Dataframe:")
for i in range(len(data_pandas)):
    print(data_pandas.iloc[i])
print("/nFirst 10 rows from numpy array:")
for row in data_numpy:
    print(row)
import pandas as pd
import numpy as np
pq=pd.read_csv('rikesh.csv')
data_pandas=pd()
data_numpy=data_pandas.to_numpy()
data_pandas.iloc[1, 11]
print(data_pandas)
import numpy as np
arr=np.array([1, 2, 3, 4])
print(arr[1],arr[3])