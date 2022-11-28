import pandas as pd

df = pd.read_csv('data.csv')

#Convert to date:
df['Date'] = pd.to_datetime(df['Date'])

#Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())
