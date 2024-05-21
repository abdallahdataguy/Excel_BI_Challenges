# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7198532970440208384-8-Ez/

import pandas as pd

# create a function to generate the required output
def insert_dash_splitter(text, size):
    length, start = len(text), len(text) % size
    result = [text[x: x + size] for x in range(start, length, size)]
    return '-'.join([text[: start]] + result if start else result)

# Read the Excel file
file_path = 'Excel_Challenge_460 - Insert Dash Splitter.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df.apply(lambda x: insert_dash_splitter(x[0], x[1]), axis=1)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the output
df
