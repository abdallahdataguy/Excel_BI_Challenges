# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7179326423331921920-tw8v/

import pandas as pd
import re

# Read the Excel file
file_path = 'Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the desired output
def split_case(text):
    chars = re.findall('[a-z]+|[A-Z]+|[0-9]+', text)
    return ', '.join(chars)

# Add the results column and print the uotput
df['My Answer'] = df['Data'].apply(split_case)
print(f'Expected Results:\n{df.iloc[:, [0, 1]]}\n\nMy Results:\n{df.iloc[:, [0, 2]]}')
