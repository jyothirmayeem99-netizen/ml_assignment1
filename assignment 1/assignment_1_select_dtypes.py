"""
Assignment 1
Check data types in pandas using DataFrame.select_dtypes()

Note: The correct pandas method name is select_dtypes(), not select_dtype().
"""

import pandas as pd


# Create a sample DataFrame with different data types
data = {
    "Name": ["Asha", "Ben", "Cara", "Dev"],
    "Age": [21, 24, 22, 25],
    "Marks": [88.5, 92.0, 79.5, 85.0],
    "Passed": [True, True, False, True],
    "Join_Date": pd.to_datetime(["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-05"]),
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nData types of all columns:")
print(df.dtypes)

# Select only integer columns
integer_columns = df.select_dtypes(include=["int64"])
print("\nInteger columns:")
print(integer_columns)

# Select only float columns
float_columns = df.select_dtypes(include=["float64"])
print("\nFloat columns:")
print(float_columns)

# Select only object/string columns
object_columns = df.select_dtypes(include=["object"])
print("\nObject/String columns:")
print(object_columns)

# Select only boolean columns
boolean_columns = df.select_dtypes(include=["bool"])
print("\nBoolean columns:")
print(boolean_columns)

# Select only datetime columns
datetime_columns = df.select_dtypes(include=["datetime64[ns]"])
print("\nDatetime columns:")
print(datetime_columns)

# Select all numeric columns: integers and floats
numeric_columns = df.select_dtypes(include=["number"])
print("\nNumeric columns:")
print(numeric_columns)

# Exclude numeric columns
non_numeric_columns = df.select_dtypes(exclude=["number"])
print("\nNon-numeric columns:")
print(non_numeric_columns)
