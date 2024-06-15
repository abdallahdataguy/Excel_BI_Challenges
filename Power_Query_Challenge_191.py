# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7207592773540057088-3q61/

import pandas as pd
import re

# Create a function to generate the required results
def extract_words(text):
    pattern1 = r'[^ A-Za-z0-9]'
    pattern2 = r'\b(\d+)([A-Z]+)\b|\b([A-Z]+)(\d+)\b'
    matches = re.findall(pattern2, re.sub(pattern1, '', text))
    joined_matches = [('_'.join(x[:2][::-1]), '_'.join(x[2:])) for x in matches]
    final_text = ', '.join([x for y in joined_matches for x in y if x != '_'])
    return final_text

# Read the Excel file
file_path = 'PQ_Challenge_191.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df = df.replace(float('nan'), '')
df['My Answer'] = df['Text'].map(extract_words)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final output
df
