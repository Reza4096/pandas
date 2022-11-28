import pandas as pd

df = pd.read_csv('data.csv')

# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

# To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace = True)

print(df.to_string())