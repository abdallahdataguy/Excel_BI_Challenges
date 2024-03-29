# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7163743730468954112-mGb-/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_392 - Collect Even and Odd from Backwards.xlsx'
df = pd.read_excel(file_path, usecols='a:b')

# Create a function to generate the required output
def collect_letters(col):
    values = list(reversed(col))
    return "".join(values[1::2] + values[::2])

# Add new column using the above function
# and print the results
df['My Answer'] = df['String'].apply(collect_letters)

print(df)
