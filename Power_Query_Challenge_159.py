# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7167005218356903936-5njT/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_159.xlsx'
df = pd.read_excel(file_path, usecols='A:D')
df.dropna(inplace=True)

# Create a DataFrame with combinations of Name, Year, and all 12 Months
# ONLY for names and years that are already in the given dataset
df2 = pd.DataFrame(
    [(n, y, m) for n in df['Name'].unique() for y in df[df['Name'] == n]['Year'].unique() for m in range(1, 13)],
    columns=['Name', 'Year', 'Month'])

# Left join with original DataFrame
df = pd.merge(df2, df, on=['Name', 'Year', 'Month'], how='left')

# Fill missing sales values with 100
df['Sales'] = df['Sales'].fillna(100)

# Change the datatypes of three columns to integer and print the output
df[['Year', 'Month', 'Sales']] = df[['Year', 'Month', 'Sales']].astype(int)

print(df)
