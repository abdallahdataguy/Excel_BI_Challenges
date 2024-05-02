# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7191285221256740866-RM27/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_446 - Top 3 Min Distance.xlsx'
df = pd.read_excel(file_path, usecols='A:H')

# Perform data transformation and cleansing
values = [sorted([df.iat[i, 0], j]) + [df.at[i, j]] 
          for i in df.index for j in df.columns[1: ] if df.at[i, j]]
df = pd.DataFrame(values, columns=['From City', 'To City', 'Distance']).drop_duplicates()
df.insert(0, 'Rank', df['Distance'].rank(method='dense').astype(int))
df = df.sort_values(by=['Rank', 'From City'], ignore_index=True)
df = df[df['Rank'] < 4]

# Display the output
print(f'\nFinal Results: \n\n{df}')
