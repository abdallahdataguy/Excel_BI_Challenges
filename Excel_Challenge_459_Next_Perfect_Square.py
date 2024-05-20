# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7198176497570893824-DZ7M/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_459 - Next Perfect Square.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df['Number'].map(lambda x: (int(x ** 0.5) + 1) ** 2)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the output
df                 
