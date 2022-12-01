import pandas as pd

data = {
    "age": [50, 40, 30, 40, 20, 10, 30],
    "qualified": [True, False, False, False, False, True, True],
}
df = pd.DataFrame(data)

# Insert "person_" before each column label:
new_df = df.add_prefix("person_")
print(new_df)

# The add_prefix() method inserts the specified value in front of the column label.
# To add a value after the column label, use the  add_suffix() method.

# Insert "_data" after each column label:
new_df = df.add_suffix("_data")
print(new_df)