# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7198895405256863745-wPaQ/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_461 - Sort the Numbers.xlsx'
df = pd.read_excel(file_path)

# Perform data manipulation
items = [(a, ''.join([x.zfill(2) for x in a.split('.')])) for a in df['String']]
items.sort(key=lambda x: x[1])
df['My Answer'] = [x[0] for x in items]
df['Check'] = df.iloc[:, 1] == df.iloc[:, 2]

# Display the final results
df
