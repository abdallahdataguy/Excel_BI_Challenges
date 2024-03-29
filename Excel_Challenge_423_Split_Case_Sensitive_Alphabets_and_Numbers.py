# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7179326423331921920-tw8v/

import pandas as pd

file_path = 'Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path)

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

df['My Answer'] = df['Data'].apply(split_case)
print(df)
