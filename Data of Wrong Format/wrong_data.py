# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong
# like if someone registered "199" instead of "1.99"

import pandas as pd

df = pd.read_csv('data.csv')
# In our example, it is most likely a typo,
# and the value should be "45" instead of "450", and we could just insert "45" in row 7:
df.loc[7,'Duration'] = 45

print(df.to_string())



# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules,
# e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:
df = pd.read_csv('data.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:  # type: ignore
    df.loc[x, "Duration"] = 120
    
print(df.to_string())


## Removing Rows
# Delete rows where "Duration" is higher than 120:
df = pd.read_csv('data.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:  # type: ignore
    df.drop(x, inplace = True)
    
print(df.to_string())
