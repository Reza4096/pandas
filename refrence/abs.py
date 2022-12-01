import pandas as pd

data = [[-50, 40, 30], [-1, 2, -2]]
df = pd.DataFrame(data)

print(df.abs())

# The abs() method returns a DataFrame with the absolute value of each value.
# This method takes no parameters.
# This function does NOT make changes to the original DataFrame object.