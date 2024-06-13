# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7206868575846834176-06h2/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_477 - Records Split and Alignment.xlsx'
df = pd.read_excel(file_path, usecols='A:B', skiprows=1)

# Perform data wrangling
starts = [y for x in df.index + 1 if (y:=(x ** 2 - x) // 2) < len(df.index)]
lengths = [x + 1 for x in range(len(lengths))]

dfs = [df.iloc[x : x + y].reset_index(drop=True) for x, y in zip(starts, lengths)]
df = pd.concat(dfs, axis=1)

df['Amount'] = df['Amount'].fillna(0).astype(int).astype(str).replace('0', '')
df['Name'] = df['Name'].replace(float('nan'), '')

# Display the final output
df
