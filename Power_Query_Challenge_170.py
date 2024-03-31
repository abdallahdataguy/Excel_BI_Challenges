# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7180051191526002688-0CgR/

import pandas as pd
import numpy as np

# Create functions to generate the required results
# Function to get column names where values match 'maximum/minimum value' per row
def matching_columns(df, row, match_col):
    matches = [col for col in df.columns if row[col] == row[match_col] and col != match_col]
    return ', '.join(matches)

# Read the Excel file
file_path = 'PQ_Challenge_170.xlsx'
df1 = pd.read_excel(file_path, usecols='E:H', nrows=2) # Original data frame
df2 = pd.read_excel(file_path, usecols='A:C') # Data frame for computation

# Add columns to the dataset and print the output
df2['Weekday'] = df2['Date'].dt.weekday
df2['Day Type'] = np.where(df2['Weekday'] < 5, 'Weekday', 'Weekend')
df2 = df2.pivot_table(values='Sale', index='Day Type', columns='Item', aggfunc='sum').fillna(0).reset_index()
df2['Total Sales'] = df2.loc[:, 'Item 1': 'Item 5'].sum(axis=1)
df2['Maximum Value'] = df2.loc[:, 'Item 1': 'Item 5'].max(axis=1)
df2['Minimum Value'] = df2.loc[:, 'Item 1': 'Item 5'].min(axis=1)
df2['Highest Selling Item'] = df2.apply(lambda x: matching_columns(df2, x, 'Maximum Value'), axis=1)
df2['Lowest Selling Item'] = df2.apply(lambda x: matching_columns(df2, x, 'Minimum Value'), axis=1)
df2 = df2.rename_axis(None, axis=1)
df2 = df2.loc[:, ['Day Type', 'Total Sales', 'Highest Selling Item', 'Lowest Selling Item']]

print(f'\nExpected Answer:\n{df1} \n\nMy Answer: \n{df2}')
