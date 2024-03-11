# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7172803509036290048-2cU-/

import pandas as pd

# Reading the Excel file
file_path = 'Excel_Challenge_409 - Table_Regular.xlsx'
df = pd.read_excel(file_path, usecols='A:E').dropna(subset=['Date'])
# fill down the missing values (forward fill - ffill)
df.ffill(inplace=True) #new in pandas 2

# Create columns by splitting variable 'Items' and add columns to original df
df = pd.concat([df, df['Items'].str.split(', ', expand=True)], axis=1)
df.drop(columns=['Items'], inplace=True)

# Unpivoting the dataframe
# Add column for sorting values while preserving the original arrangement
df['Ordering'] = range(len(df))
keep_columns = ['Categories', 'Date', 'Companies', 'Note','Ordering'] # Columns to keep as is
unpivot_columns = list(range(6)) # Columns to unpivot
df = pd.melt(df, id_vars=keep_columns, var_name='Variable', value_name='Items') # Unpivot the df

# Cleaning the dataframe
df.sort_values(by=['Ordering', 'Variable'], inplace=True)
df = df.loc[:, ['Categories', 'Date', 'Items', 'Companies', 'Note']]
df.dropna(subset=['Items'], inplace=True, ignore_index=True)

# Print the dataframe
print(df)
