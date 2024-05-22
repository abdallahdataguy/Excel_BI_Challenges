# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7198895405256863745-wPaQ/

import pandas as pd
import re

# Read the Excel file
file_path = 'Excel_Challenge_461 - Sort the Numbers.xlsx'
df = pd.read_excel(file_path)

# Perform data manipulation
df['My Answer'] = sorted(df['String'], key=lambda x: re.sub('\d+', lambda y: y.group().zfill(2), x))
df['Check'] = df.iloc[:, 1] == df.iloc[:, 2]

# Display the final results
df
