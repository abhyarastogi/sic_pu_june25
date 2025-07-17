# Reading a CSV file and checking for missing values

# Explanation: Using pd.read_csv() to load data and checking for missing values using isnull()
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False) # Stores the dataframe into a csv file
df = pd.read_csv('data.csv')  # Reads the CSV file
print(df)
df.head()  # Displays the first 5 rows
print(df.isnull().sum())  # Counts missing values in each column