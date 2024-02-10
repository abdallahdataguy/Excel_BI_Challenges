# Link to the challenge: https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7160844652193984512-GlNM

import re
import pandas as pd

# Specify a file name
file_name = 'Excel_Challenge_386 - Extract Numbers in Parentheses.xlsx'

# Read the file
df = pd.read_excel(file_name)

# Create a function to extract the numbers in parentheses given a string
def answer(col):
    return ", ".join(re.findall(r'\((\d+)\)', col))
    
# Add a new colum 'My Answer' to the dataframe using the function above
df['My Answer'] = df['String'].apply(answer)

# Replace empty string values by na values
df['My Answer'] = df['My Answer'].replace('', float('nan'))

print(df)
