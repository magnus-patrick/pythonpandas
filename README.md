# Pandas 🐼

-Programming with the Pandas library!

-"Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language."

import pandas as pd

df = pd.read_csv('pokemon_data.csv') #Reads a CSV file.

# df.columns (All the headers.)
# df.head(N) (First N rows.)
# df.tail(N) (Last N rows.)

## Read each row.
# df.iloc[10:50]

## Read each column.
# df[['Name', 'Type 1']]

## Read specific location.
# df.iloc[2, 1]  Written as: df[Row, Column]

## One condition and multiple conditions.
# df[df['Type 2'] == 'Psychic']
# df[(df['Type 1'] == 'Fire') & (df['HP'] > 100)]

## Sorting values alphabetically or by greatest or least.
# df.sort_values(['Name', 'Attack'], ascending = [0, 1]) 1 means ascending, 0 means descending.
# df.sort_values('Attack', ascending = False)

## Making a new column.
# df['Total'] = df['Attack'] + df['Defense']
# df['Total'] = df.iloc[:, 4:10].sum(axis = 1)
# df.head(50)

## Removing columns.
# df.drop(columns = ['Speed'])

## Saves data as a CSV, Excel, or text file respectively.
# df.to_csv('newpoke.csv', index = False) "index = False removes indexes on left side."
# df.to_excel('newpoke.xlsx', index = False)
# df.to_csv('newpoke.txt', index = False, sep = '\t') "Keyword sep separates values by tabs instead of commas."

# ndf = df[(df['Type 1'] == 'Fire') & (df['HP'] > 100)]
# ndf.reset_index(drop = True, inplace = True) "drop keyword removes original indexes, amd inplace conserves memory."

## Filtering out certain words or characters.
# df[~df['Name'].str.contains('Mega')] "~ character filters out words."

## Currently, I am not too familiar with the re or regular expressions module.
# import re
# df[df['Name'].str.contains('fire|grass', flags = re.I, regex = True)] 

