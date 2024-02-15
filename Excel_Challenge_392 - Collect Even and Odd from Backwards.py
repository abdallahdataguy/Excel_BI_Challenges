# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7163743730468954112-mGb-/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_392 - Collect Even and Odd from Backwards.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the required output
def collect_letters(col):
    even, odd = [], []      # unpacking
    for ind, char in enumerate(reversed(list(col))):
        even.append(char) if ind % 2 else odd.append(char)      # conditional expression            
    return "".join(even + odd)

# Add new column using the above function
# and print the results
df['My Answer'] = df['String'].apply(collect_letters)

print(df)
