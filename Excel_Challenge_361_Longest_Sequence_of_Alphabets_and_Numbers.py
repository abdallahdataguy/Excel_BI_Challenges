# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7148161188114190336--Mvk/

import pandas as pd
import re

# Read the Excel file
file_path = 'Excel_Challenge_361 - Longest Sequence of Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path)
df.replace(float('nan'), '', inplace=True)
df = df.astype(str)

# Perform data transformation and cleansing
def longest_sequence(col):
    chars = re.findall(r'([a-zA-Z]*)', col)    
    nums = re.findall(r'(\d*)', col)
    alphabets  = ', '.join([x for x in chars if len(x) == max([len(y) for y in chars]) and x != ''])
    numbers  = ', '.join([x for x in nums if len(x) == max([len(y) for y in nums]) and x != ''])
    return alphabets, numbers

df[['My Alphabets', 'My Numbers']] = df['String'].apply(longest_sequence).tolist()
df['Correct'] = df.apply(
    lambda x: (x['Alphabets'] == x['My Alphabets']) & (x['Numbers'] == x['My Numbers']), axis=1)

# Display the output
df
