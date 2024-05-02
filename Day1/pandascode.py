import pandas as pd

# Create a dictionary of data
data = {'Name': ['John', 'Emma', 'Peter', 'Olivia'],
    'Age': [25, 28, 30, 27],
    'City': ['New York', 'London', 'Paris', 'Tokyo']}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)