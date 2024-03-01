# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7169179556946329600-4n_0/

import pandas as pd

# Read the Excel file
file_path = r'C:\Users\aally\Downloads\Excel_Challenge_403 - Generate Pivot Table.xlsx'
df1 = pd.read_excel(file_path, usecols='A:B', index_col=0)
df2 = pd.read_excel(file_path, usecols='D:F', skiprows=1).dropna()
df2['% of Value'] = df2['% of Value'].map(lambda x: f"{int(round(x * 100))}%")
df2['Sum of Value'] = df2['Sum of Value'].astype(int)

# Create a dataset of grouped values
base, interval = 1990, 5
# Create Sum of Values column
df1 = df1.groupby((df1.index - base) // interval * interval)[['Value']].sum()

# Create a percent of vlaues column and format the values to include 
# percentage symbol
df1['% of Value'] = (df1['Value'] / df1['Value'].sum())*100
df1['% of Value'] = df1['% of Value'].map(lambda x: f"{int(round(x))}%")

# Create year interval labels and set it as a row index
df1['Year'] = df1.index.map(lambda x: f"{base + x}-{base + x + interval - 1}")
df1.set_index('Year', inplace=True)

# Make row index as a new column and use default indexes 0 => n
df1.reset_index(inplace=True)

# Add a grand total as a last value to a dataframe
df1.loc[len(df1)] = ('Grand Total', df1['Value'].sum(), '100%')
# Rename 'Value' column to a 'Sum of Value' Column
df1.rename(columns={'Value': 'Sum of Value'}, inplace=True)

print(f'\nExpected Answer: \n{df2} \n\nMy Answer: \n{df1}')