# import pandas as pd
# df=pd.read_csv('machine.csv')
# print("Dataset Information:")
# total_rows=len(df)
# print("/nfirst 20 rows")
# print(df[:20])
# print("/nlast 20 rows:")
# print(df[total_rows-20:])
# import pandas as pd
# df = pd.read_csv('machine.csv')
# print("Dataset Information:")
# total_rows = len(df)
# print("\nFirst 20 rows:")
# for i in range(min(20, total_rows)):
#     print(df.iloc[i])
# print("\nLast 20 rows:")
# for i in range(max(0, total_rows - 20), total_rows):
#     print(df.iloc[i])
import pandas as pd
df=pd.read_csv('machine.csv')
X=[]
rows=df.values
for i in range(1,21 ):
    print()