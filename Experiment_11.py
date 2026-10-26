import pandas as pd
import numpy as np

# 1. Create a Series with 10 random numbers
numbers = np.random.randint(1, 100, 10)
ser = pd.Series(numbers)
print("Pandas Series:")
print(ser)

# 2. Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 30],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 52000, 58000]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# 3. Indexing and selecting data
print("\nName Column:")
print(df['Name'])

print("\nFirst Row:")
print(df.iloc[0])

print("\nEmployees in IT:")
print(df[df['Department'] == 'IT'])

# 4. Data cleaning
df.loc[1, 'Age'] = np.nan
print("\nMissing Values:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.drop_duplicates()

print("\nCleaned DataFrame:")
print(df)

# 5. Merge two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Salary': [60000, 52000, 45000]
})

merged = pd.merge(df1, df2, on='ID', how='inner')
print("\nMerged DataFrame:")
print(merged)

# 6. Grouping and aggregation
print("\nAverage Salary by Department:")
print(df.groupby('Department')['Salary'].mean())

print("\nSalary Statistics by Department:")
print(df.groupby('Department')['Salary'].agg(
    ['mean', 'sum', 'max', 'min']
))