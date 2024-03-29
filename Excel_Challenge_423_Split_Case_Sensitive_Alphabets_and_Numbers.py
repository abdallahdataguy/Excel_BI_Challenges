# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7179326423331921920-tw8v/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path)

# Create functions to generate the desired output
def case(char):
    if ord(char) in range(97, 123): return 'lower'
    if ord(char) in range(65, 91): return 'upper'
    if ord(char) in range(48, 58): return 'digit'

def split_case(text):
    chars = ''
    for i in range(len(text) - 1):
        if case(text[i]) == case(text[i + 1]):
            chars += text[i]
        else:
            chars += text[i] + ', '
    return chars + text[-1]
pd.set_option('display.max_columns', 5)

# Add the results column and print the uotput
df['My Answer'] = df['Data'].apply(split_case)
print(f'Expected Results:\n{df.iloc[:, [0, 1]]}\n\nMy Results:\n{df.iloc[:, [0, 2]]}')
