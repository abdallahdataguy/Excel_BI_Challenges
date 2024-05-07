# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7193459554162982912-rADF/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_450 - Ranking.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
df['My Answer'] = df.groupby('Company')['Sales'].rank(method='dense', ascending=False)

# Codes below just to make a diplay (int) same as the one in Excel
# By default pandas converts columns with missing values to float
# Otherwise the single line of code above with groupby would suffice
df[df.columns[1:]] = df[df.columns[1:]].fillna('0')
df[df.columns[2:]] = df[df.columns[2:]].astype(int).astype(str)
df = df.replace('0', '')

# Display results
df
