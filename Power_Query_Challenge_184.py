# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7197805781231030272-IN3B/

import pandas as pd
import re

# read the Excel file
file_path = 'PQ_Challenge_184.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data wrangling
def extract_alphabets(text):
    text = re.findall('[a-zA-Z]+\d+', text)
    return text[-1] if text else ''
    
df['Alphabets'] = df.iloc[:, 1].map(extract_alphabets)
df = df.groupby('Set').agg(
    Text = ('Alphabets', lambda x: '-'.join(x[x != ''])),
    Original_Count = ('Set', 'count'),
    New_Count = ('Alphabets', lambda x: x[x != ''].count())
    ).reset_index()
df = df.rename(columns={'Original_Count': 'Original Count',
                       'New_Count': 'New Count'})

# Display the output
df
