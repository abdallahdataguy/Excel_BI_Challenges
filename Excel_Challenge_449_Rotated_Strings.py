# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7193097156491100160-pmwm/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_449 - Rotated Strings.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data transformation and cleansing
strings = [x[1].values for x in df.iterrows() if (x[1][0] * 2).find(x[1][1]) > 0
          and len(x[1][0]) == len(x[1][1])]
df = pd.DataFrame(strings, columns=['MyString1', 'MyString2'])

# Display the output
df
