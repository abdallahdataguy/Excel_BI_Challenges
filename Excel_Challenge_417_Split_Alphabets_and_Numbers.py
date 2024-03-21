# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7176427310550573056-u5IQ/

import pandas as pd

# Read the Excel file
file_path = r'C:\Users\aally\Downloads\Excel_Challenge_417 - Split Alphabets and Numbers.xlsx'
df = pd.read_excel(file_path)

# Create a function that generates the required results
def split_chars(col):
    chars = ''
    for i in range(len(col) - 1):
        a = (ord(col[i].upper()) - 48) in range(10)
        b = (ord(col[i + 1].upper()) - 48) in range(10)
        if not a == b:
            chars += col[i] + ', '
        else:
            chars += col[i]
    return chars + col[-1]

# Add new column to get the required results
df['My Answer'] = df['Data'].apply(split_chars)

# Print the output
df1, df2 = df[['Data', 'Expected Answer']], df[['Data', 'My Answer']]
print(f'Expected Results:\n{df1}\n\nMy Results:\n{df2}')
