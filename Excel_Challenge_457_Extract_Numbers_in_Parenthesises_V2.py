# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7196721087445946368-KeCD/
# This solution ONLY works with matching pair of parentheses (), [] or {}

import pandas as pd
import re

# Read the Excel file
file_path = 'Excel_Challenge_457 - Extract Numbers in Parenthesises.xlsx'
df = pd.read_excel(file_path).astype(str).replace('nan', '')

# Perform data transformation and cleansing
pattern = '\[(\d+)\]|\{(\d+)\}|\((\d+)\)'
df['My Answer'] = df['String'].apply(lambda x: ', '.join([''.join(a) for a in re.findall(pattern, x)]))
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display Results
df
