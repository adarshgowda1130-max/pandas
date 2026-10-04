#pandas
#series=single column,dataframe=multiple columns(like a table)
import pandas as pd
import numpy as np

# Creating a Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name="Scores")

# Creating a DataFrame from a dictionary
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, 40, 22],
#     'City': ['New York', 'London', 'Paris', 'London', 'New York'],
#     'Salary': [70000, 85000, 95000, 60000, 52000]
# }
data=pd.read_csv("output.csv")#reads data from csv file and stores it in a dataframe
df = pd.DataFrame(data)
print(df)
print(df.head(3))         # First 3 rows
print(df.tail(2))         # Last 2 rows
print(df.info())          # Column names, data types, and non-null counts
print(df.describe())      # Summary statistics for numerical columns
print(df.shape)           # Tuple of (rows, columns)
print(df.columns)            # List of column names
print(df.dtypes)          # Data types of each column