# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7196358657284935683-TIWl/

import pandas as pd
import re

# Create a function to generate the required output
def extract_special_Characters(col):
    return re.sub('[^_\W]', '', col) # => [a-zA-Z0-9]

# Read the Excel file
file_path = 'Excel_Challenge_456 -Extract special Characters.xlsx'
df = pd.read_excel(file_path).replace(float('nan'), '')

# Perform data transformation and cleansing
df['My Answer'] = df['String'].apply(extract_special_Characters)
df['Check'] = df['Expected Answer'] == df['My Answer']

# Display results
df
