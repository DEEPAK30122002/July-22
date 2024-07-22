import pandas as pd

# Read data from the CSV file
df = pd.read_csv('data.csv')

# Display the entire DataFrame
print("Original DataFrame:")
print(df)
print()

# Perform operations on the DataFrame as needed
average_age = df['Age'].mean()
print(f"Average Age: {average_age}")
print()

# Example: Filter the DataFrame based on a condition
older_than_30 = df[df['Age'] > 30]
print("People older than 30:")
print(older_than_30)
