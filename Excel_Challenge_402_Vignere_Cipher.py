# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7168817160763518977-ySFj/

import pandas as pd
from math import ceil

# Read the Excel file
file_path = 'Excel_Challenge_402 - Vignere Cipher.xlsx'
df = pd.read_excel(file_path, usecols='A:C')

# Create a function to generate the required output
def vignere_cipher(col1, col2):
    encrypted_text = ''
    text = col2 * ceil(len(col1) / len(col2))
    for i in range(len(col1)):
        if col1[i] == ' ':
            text = text[:i] + ' ' + text[i:]
    for i in range(len(col1)):
        if col1[i] == ' ':
            encrypted_text += ' '
        else:
            encrypted_text += chr(((ord(col1[i]) + ord(text[i]) - 194) % 26) + 97)
    return encrypted_text

# Add results column to the dataset using the function developed above
df['My Answer'] = df.apply(lambda x: vignere_cipher(x['Plain Text'], x['Keyword']), axis=1)

print(df)
