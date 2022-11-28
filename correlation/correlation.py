import pandas as pd

df = pd.read_csv('data.csv')

# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.
print(df.corr())

# Note: The corr() method ignores "not numeric" columns.

# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# The number varies from -1 to 1.
# 1 means that there is a 1 to 1 relationship (a perfect correlation),
# and for this data set, each time a value went up in the first column,
# the other one went up as well.
# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.