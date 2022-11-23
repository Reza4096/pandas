import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

## Locate Row
#refer to the row index:
print(df.loc[0])

#use a list of indexes:
print(df.loc[[0, 1]])
