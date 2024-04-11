# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7184037452787924992-Cn5R/

import pandas as pd
from string import ascii_lowercase
from math import ceil

# Read the Excel file
file_path = 'Excel_Challenge_432 - Bifid Cipher_Part 1.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def bifid_cipher(col):
    values = []
    for index, char in enumerate(ascii_lowercase.replace('j', ''), start=1):
        i = ceil(index / 5)
        j = index - (index // 5) * 5
        values.append((char, str(i), str(5 if j == 0 else j)))
    s1 = [x[1] for char in col.replace('j', 'i') for x in values if char == x[0]]
    s2 = [x[2] for char in col.replace('j', 'i') for x in values if char == x[0]]
    string = ''.join(s1 + s2)
    encrypted_string = ''
    for i in range(0, len(string), 2):
        sample = string[i: i + 2]
        for value in values:
            if sample[0] == value[1] and sample[1] == value[2]:
                encrypted_string += value[0]
    return encrypted_string

df['My String'] = df['Plain Text'].apply(bifid_cipher)

# Print the output
print(f'\nExpected Results:\n{df.iloc[:, [0, 1]]}\n\nMy Results:\n{df.iloc[:, [0, 2]]}')
