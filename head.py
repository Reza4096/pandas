import pandas as pd

df = pd.read_csv('data.csv')

#The head() method returns the headers and a specified number of rows, starting from the top.
print(df.head(10))

#if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head())

#The tail() method returns the headers and a specified number of rows, starting from the bottom.
print(df.tail())

#The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())