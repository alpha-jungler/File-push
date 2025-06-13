# import pandas as pd
# data = [10, 20, 30, 40]
# series = pd.Series(data, index=['a', 'b', 'c', 'd'])
# print(series.to_string())
# import pandas as pd
# X=pd.Series('machine.csv')
# print(X.to_string()) 
# import pandas as pd
# data = [10, 20, 30, 40]
# series = pd.Series(data, index=['a', 'b', 'c', 'd'])
# print(series)

import pandas as pd
df = pd.read_csv('machine.csv')
print("First 5 rows of the datas")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe(include='all'))
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
print("\nData Types of Each Column:")
print(df.dtypes)
numeric_cols = df.select_dtypes(include=['float64', 'int64'])
if numeric_cols.shape[1] > 1:
    print("\nCorrelation Matrix:")
    print(numeric_cols.corr())
else:
    print("\nNot enough numeric columns for correlation matrix.")
