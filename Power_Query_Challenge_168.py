# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7177514489527877632-m3FP/

import pandas as pd

# Read the Excel file
file_path = 'Power_Query_Challenge_168.xlsx'
df1 = pd.read_excel(file_path, usecols='A:B') # Data frame for transformation
df2 = pd.read_excel(file_path, usecols='D:E') # Data frame for comparison
df2.columns = df2.columns.str.replace('.1', '')

# Data transformation and cleansing
df1.sort_values(by=['Store', 'Item'], inplace=True, ignore_index=True)
combinations = []
for i in df1['Item'].index:
    if i == 0 or df1['Store'][i] != df1['Store'][i - 1]:
        combination = df1['Item'][i]
    else:
        combination += "/" + df1['Item'][i]
    combinations.append(combination)
df1['Item'] = pd.Series(combinations)

# Print the required output
print(f'\nExpected Results:\n{df2}\n\nMy Results:\n{df1}')

