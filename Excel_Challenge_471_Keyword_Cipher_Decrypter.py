# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7203983569814274048-0tDz/

import pandas as pd
from string import ascii_lowercase

# Create a function to generate the required results
def decrypter(text1, text2):
    string1 = ascii_lowercase
    string2 = ''.join(list(dict.fromkeys(text2 + string1)))
    text = ''
    for char in text1:
        if char == ' ': text += ' '
        else: text += string1[string2.find(char)]
    return text

# Read the Excel file
file_path = 'Excel_Challenge_471 - Keyword Cipher Decrypter.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df.apply(lambda x: decrypter(x[0], x[1]), axis=1)
df['Check'] = df['My Answer'] == df['Answer Expected']

# Display the final results
df
