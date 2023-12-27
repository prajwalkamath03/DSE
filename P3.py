import pandas as pd
df=pd.read_csv('dataa.csv')

print("First few rows: ")
print(df.head())

print("\nSummary stats")
print(df.describe())

filtered_data=df[df['Age']>30]
print("\nFiltered data(Age>30)")
print(filtered_data)

sorted_data=df.sort_values(by='Salary',ascending=False)
print("\nSorted data(by salary):")
print(sorted_data)

df["Bonus"]=df['Salary']*0.1
print("\nData with new column (Bonus): ")
print(df)

df.to_excel('output.xlsx',index=False)
print("\nData written to output.xlsx")

