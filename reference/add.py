import pandas as pd

data = {"points": [100, 120, 114], "total": [350, 340, 402]}

df = pd.DataFrame(data)

print(df.add(15))

# The add() method adds each value in the DataFrame with a specified value.
# The specified value must be an object that can be added to the values of the DataFrame.
# It can be a constant number like the one in the example,
# or it can be a list-like object like a list [15, 20] or a tuple {"points": 380, "total": 22},
# or a  Pandas Series or another DataFrame, that fits with the original DataFrame.

print(df.add([15, 20]))
print(df.add({"points": 380, "total": 22}))  # type: ignore
print(df.add(pd.Series([10, 20], index=["points", "total"])))
print(df.add(df))


## Syntax
# dataframe.add(other, axis, level, fill_value)

### Equivalent to dataframe + other,
# but with support to substitute a fill_value for missing data in one of the inputs.
# With reverse version, radd.

print(df + 1)
print(df + [15, 20])
print(df + {"points": 380, "total": 22})
print(df + pd.Series([10, 20], index=["points", "total"]))
print(df + df)