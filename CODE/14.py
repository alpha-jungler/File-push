# import pandas as pd 
# datas={'name':['Kirtan', 'Rikesh', 'Lizen'], 'age':[16, 16, 17], 'city':['Kathmandu', 'Bhaktapur', 'Lalitpur']}
# df=pd.DataFrame(datas)
# print(df)

# data = [{'ID': i, 'Name': f'Person_{i}', 'Age': 20 + (i % 10)}
#     for i in range(1, 21)]
# df = pd.DataFrame(data)
# print("Head (First 5 rows):")
# print(df.head())
# print("\nTail (Last 5 rows):")
# print(df.tail())
import pandas as pd
X={'Name':['Rozen', 'Ranjit', 'Newson'], 'Age':[17, 16, 18], 'City':['Kathmandu', 'Dolkha', 'Bhimsenpur'], 'Grade':[11, 12, 12], 'Favourite fruits':['Apple', 'Mango', 'Orange'], 'Lucky numbers':[9, 7, 2], 'Caste':['Tamang', 'Thakuri', 'Karki'], 'House number':[26, 1, 4], 'Location':['Dhobidhara', 'Bagbazar', 'Ghattekulo'], 'Ward number':[30, 26, 19], 'College':['Times', 'Golden Gate', 'Trinity'], 'Favourite number':[6, 8, 7], 'Permanent address':['Shisanya', 'Chitwan', 'Dolkha'], 'Gate number':[48, 84, 92], 'Temporary address':['Dhobidhara', 'Bagbazar', 'Ghattekulo'], 'Family members':[9, 4, 6], 'Favourite place':['Bouddhanath stupa', 'Solukhumbu', 'Sudhurpachhim'], 'Ward no':[30, 26, 19], 'Favourite car':['Mustang GTR', 'Lamborghini', 'Supra'], 'Car no':[19, 18, 17] }
df=pd.DataFrame(X)
print("Head(first 5 rows):")
print(df.Head())
print("/nTail(last 5 rows):")
print(df.tail())
