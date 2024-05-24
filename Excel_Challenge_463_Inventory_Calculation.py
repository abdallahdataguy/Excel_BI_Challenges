# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7199635229140004866-Mt0W/

import pandas as pd
from datetime import datetime

# Read the Excel file
file_path = 'Excel_Challenge_463 - Inventory Calculation.xlsx'
df1 = pd.read_excel(file_path, usecols='A:C', nrows=5)

# Perform data wrangling
months = [datetime(2023, x , 1).strftime('%b') for x in range(1, 13)]
df2 = pd.DataFrame(months, columns=['Month'])
df = df2.merge(df1, how='left')
df['Inventory'] = (df.iloc[:, 1] - df.iloc[:, 2]).fillna(0).cumsum().map(int)
df = df.iloc[:, [0, 3]]

# Display the output
df
