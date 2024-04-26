# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7189473285099704320-i3s1/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_443 - Birds Search.xlsx'
df1 = pd.read_excel(file_path, usecols='B:K', skiprows=0)
df2 = pd.read_excel(file_path, usecols='M', nrows=7)

# Perform data transformation and cleansing
joined_chars = [''.join(x) for x in df1.values]
words1 = []
for x in joined_chars:
    for y in df2.Birds:
        x = x.replace(y, y.upper())
    words1.append(x)

words2 = []
for x in words1:
    word = ''
    for y in x:
        if y.islower(): word += 'x'
        else: word += y.lower()
    words2.append(word)

df = pd.DataFrame([list(x) for x in words2])

# Print the output
df
