# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7204693554764406784-e5Nc/

import pandas as pd

# Create a function to generate the required output
def ascii_words(word):
    a = '   ' + ''.join(['_   ' if char != ' ' else '  ' for char in word])[:-1] + '\n'
    b = '  ' + ''.join(['/ \ ' if char !=' ' else '  ' for char in word]) + '\n'
    c = ' ' + ''.join(['| ' + (char + ' ' if char != ' ' else '') for char in word]) + '|\n'
    d = '  ' + ''.join(['\_/ ' if char !=' ' else '  ' for char in word]) 

    return a + b + c + d

# Read the Excel file
file_path = 'Excel_Challenge_473 - ASCII Words.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df['Words'].map(ascii_words)
df['Check'] = df['My Answer'] == df['Answer Expected']

# Print the final results
for word in df['Words']:
    print(ascii_words(word))

# Display the final dataset
df
