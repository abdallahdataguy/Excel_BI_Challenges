# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7179688805430398976-XrX3/

import pandas as pd
import re

# Read the Excel file
file_path = 'PQ_Challenge_169.xlsx'
df1 = pd.read_excel(file_path, usecols='C:D').replace(float('nan'), '') # Original data frame
df1.rename(columns={'String.1': 'String'}, inplace=True)

df2 = pd.read_excel(file_path, usecols='A') # Data frame for computation

# Create a function to generate the required results
def extract_words(text):
    chars = re.findall(r'\b[A-Z]+[0-9]+[A-Z0-9]*\b', text)
    return ', '.join(chars)

# Add results column to the dataset and print the output
df2['My Codes'] = df2['String'].apply(extract_words)

print(f'\nExpected Answer: \n{df1} \n\nMy Answer: \n{df2}')
