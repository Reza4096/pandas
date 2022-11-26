import pandas as pd

df = pd.read_csv('data.csv')

#Return a new Data Frame with no empty cells:
new_df = df.dropna()

print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:
df.dropna(inplace = True)
print(df.to_string())

## Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
print(df.to_string())

# To only replace empty values for one column, specify the column name for the DataFrame:
df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)