# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7186574164361633792-8kW3/

import pandas as pd
from string import ascii_lowercase
from math import ceil

# Create a function to generate the required results
def bifid_cipher2(col1, col2):
    characters = ''
    text = col2.replace('j', 'i') + ascii_lowercase.replace('j', '')
    for char in text:
        if char not in characters:
            characters += char
    values = []
    for index, char in enumerate(characters, start=1):
        i = ceil(index / 5)
        j = index - (index // 5) * 5
        values.append((char, str(i), str(5 if j == 0 else j)))
    text1 = [x[1] for char in col1.replace('j', 'i') for x in values if char == x[0]]
    text2 = [x[2] for char in col1.replace('j', 'i') for x in values if char == x[0]]
    text = ''.join(text1 + text2)
    encrypted_text = ''
    for i in range(0, len(text), 2):
        sample = text[i: i + 2]
        for value in values:
            if sample[0] == value[1] and sample[1] == value[2]:
                encrypted_text += value[0]
    return encrypted_text

# Read the Excel file, perform data transformation and cleansing
file_path = 'Excel_Challenge_437 - Bifid Cipher_Part 2.xlsx'
df = pd.read_excel(file_path)
df['My Answer'] = df.apply(lambda x: bifid_cipher2(x['Plain Text'], x['Keywords']), axis=1)

# Display the output
df
