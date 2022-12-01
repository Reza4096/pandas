import pandas as pd

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}

df = pd.DataFrame(data)

# Return the sum of each row:
x = df.agg(["sum"])
print(x)

# The agg() method allows you to apply a function or a list of function names to be executed
# along one of the axis of the DataFrame,
# default 0, which is the index (row) axis.

## Syntax
# dataframe.agg(func, axis, args, kwargs)

x = df.agg(["sum","min"])
print(x)

x = df.agg([sum,max])
print(x)