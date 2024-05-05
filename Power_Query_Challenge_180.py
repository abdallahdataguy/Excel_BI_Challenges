# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7192734760387960832-6Zh_/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_180.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data transformation and cleansing
df['Emp'] = df['Emp-Month'].where(cond=pd.isnull(df['Sales']), other=float('nan')).ffill()
df = df.dropna(subset='Sales').reset_index(drop=True)
df['Order'] = df.groupby('Emp').cumcount()
df['Sales Change'] = (df['Sales'] - df['Sales'].shift(1)).where(df['Order'] > 0, float('nan')).abs()
df['From - To Months'] = (df['Emp-Month'].shift(1) + ' - ' + df['Emp-Month']).where(df['Order'] > 0, float('nan'))
df['Total Sales'] = df.groupby('Emp')['Sales'].transform('sum').astype(int)
df['Max Sales Change'] = df.groupby('Emp')['Sales Change'].transform('max').astype(int)
df = df[df['Sales Change'] == df['Max Sales Change']]
df = df.iloc[:, [2, 6, 7, 5]].reset_index(drop=True)

# Display the output
df
