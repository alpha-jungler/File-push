import pandas as pd
import numpy as np
p=pd.read_csv('pandas/machine.csv')
data_pandas=p.head(50)
data_pandas=p.tail(50)
data_numpy=data_pandas.to_numpy()
print("first 50 rows from pandas DataFrame:")
for i in range(len(data_pandas)):
    print(data_pandas.iloc[i])
for row in data_numpy:
    print(row)