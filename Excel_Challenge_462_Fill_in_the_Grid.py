# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7199257736868454400-HJhU/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_462 - Fill in the Grid.xlsx'
dfo = pd.read_excel(file_path, skiprows=1, nrows=10, header=None) # Original df

# Perform data wrangling
# Create a function to generate the required results
def custom_fillna(df):
    dfs = [df.shift(1), df.shift(-1), # axis=0, default
           df.shift(1, axis=1), df.shift(-1, axis=1), 
           df.shift(1).shift(1, axis=1), df.shift(1).shift(-1, axis=1),
           df.shift(-1).shift(1, axis=1), df.shift(-1).shift(-1, axis=1)
          ]
    for i in df.index:
        for j in range(len(df.columns)):
            if pd.isnull(df.iat[i, j]):
                df.iat[i, j] = max([x.iat[i, j] for x in dfs])
    return df.astype(int)

# Create a requred data frame          
df = custom_fillna(dfo)

# Display the output
df
