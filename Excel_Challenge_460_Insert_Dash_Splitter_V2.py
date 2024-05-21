# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7198532970440208384-8-Ez/

import pandas as pd
import re

# Read the Excel file
file_path = 'Excel_Challenge_460 - Insert Dash Splitter.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df.apply(lambda x: '-'.join(
    re.findall(f'.{{1,{x[1]}}}(?=(?:.{{{x[1]}}})*$)', x[0])), axis=1)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the output
df
