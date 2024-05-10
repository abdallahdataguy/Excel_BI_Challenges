# Link to the challenge
# coding: utf-8

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_453 - Common in Columns.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data transformation and cleansing
c, d = df.columns
fruits = [(x, min([sum(df[c] == x), sum(df[d] == x)])) 
          for x in df[c].unique() if x in df[d].values]

df = pd.DataFrame(fruits, columns=['Match', 'Count'])

# Display final results
df
