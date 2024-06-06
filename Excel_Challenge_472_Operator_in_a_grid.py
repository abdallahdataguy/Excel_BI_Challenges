# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7204331171202113536-iPny/

import pandas as pd
pd.set_option('display.float_format', '{:.4f}'.format)

# Read the Excel file
file_path = 'Excel_Challenge_472 - Operator in a grid.xlsx'
df = pd.read_excel(file_path, usecols='A:I').dropna(axis=1)

# Perform data wrangling
df['My Answer'] = df.apply(lambda x: eval(''.join(x[:-1].map(str))), axis=1)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
