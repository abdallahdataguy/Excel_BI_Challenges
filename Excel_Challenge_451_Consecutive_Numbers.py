# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7193821970638000128-AJpt/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_451 - Consecutive Numbers.xlsx'
df = pd.read_excel(file_path, usecols='A')

# Perform data transformation and cleansing
df['serial'] = df.groupby((df['Numbers'] != df['Numbers'].shift(1)).cumsum()).cumcount() + 1
max_pos = df['serial'][df['Numbers'] > 0].max()
max_neg = df['serial'][df['Numbers'] < 0].max()
pos_values = ', '.join([str(x) for x in df['Numbers'][(df['serial'] == max_pos) & (df['Numbers'] > 0)].unique()])
neg_values = ', '.join([str(x) for x in df['Numbers'][(df['serial'] == max_neg) & (df['Numbers'] < 0)].unique()])

# Create a final data frame
ind = ['Max Consecutive Positive Number', 'Max Consecutive Negative Number']
col = ['Number', 'Count']
df = pd.DataFrame([[pos_values, max_pos], [neg_values, max_neg]], index=ind, columns=col)

# Display the results
df
