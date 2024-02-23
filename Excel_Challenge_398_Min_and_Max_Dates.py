# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7166642838963699712-Ja5K/

import pandas as pd

# read the Excel file
file_path = 'Excel_Challenge_398 - Min and Max Dates.xlsx'
df1 = pd.read_excel(file_path, header=1, usecols='C:F').dropna()
df1[['Year', 'Month']] = df1[['Year', 'Month']].astype(int)
df2 = pd.read_excel(file_path, usecols='A')

# Extract year and month
df2['Year'] = df2['Date'].dt.year
df2['Month'] = df2['Date'].dt.month

# Group by year and month, and calculate min and max dates
df2 = df2.groupby(['Year', 'Month'])['Date'].agg(['min', 'max'])

# Rename columns
df2.rename(columns={'min': 'Min Date', 'max': 'Max Date'}, inplace=True)

# Reset index to make 'Year' and 'Month' columns
df2.reset_index(inplace=True)

# Display the first five records
print(f'\nAnswer Expected: \n{df1.head()}')
print(f'\nMy Answer: \n{df2.head()}')
