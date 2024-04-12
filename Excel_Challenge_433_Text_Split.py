# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7184399850711486464-k43d/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_433 - Text Split.xlsx'
df = pd.read_excel(file_path, usecols='A')

# Perform data transformation and cleansing
def text_split(col):
    levels = col[ : col.find(' ')].split('.')
    levels = levels + [''] * (3 - len(levels))
    names = col.split(' ')[-2: ]
    return levels + names

columns = ['Level', 'Level2', 'Level3', 'First Name', 'Last Name']
df[columns] = df['Text'].apply(text_split).tolist()

# Print the output
print(f'\nMy Results\n{df}')
