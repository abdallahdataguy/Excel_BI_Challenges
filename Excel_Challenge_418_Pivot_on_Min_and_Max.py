# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7176789688647573505-0c2a/

import pandas as pd

# Read the Excel file as two dataframes to be used for comparison
file_path = 'Excel_Challenge_418 - Pivot on Min and Max .xlsx'
df1 = pd.read_excel(file_path, usecols='E:G', nrows=12) # required results
df1.rename(columns={'Date.1': 'Date', 'Emp ID.1': 'Emp ID'}, inplace=True)
df2 = pd.read_excel(file_path, usecols='A:C') # df for computation

# Groupby to calculate minimum and maximum time per Emp ID and Date
df2 = df2.groupby(['Date', 'Emp ID'])['Time'].agg(['min', 'max']).reset_index()

# Unpivot the aggregate columns min max columns
df2 = pd.melt(df2, id_vars=['Date', 'Emp ID'], value_vars=['min', 'max'], value_name='Min & Max Time')
df2.sort_values(by=['Date', 'Emp ID', 'variable'], ascending=[True, True, False], inplace=True)
df2 = df2[['Date', 'Emp ID', 'Min & Max Time']]

# Print the output
print(f'\nExpected Results:\n{df1}\n\nMy Results:\n{df2}')

