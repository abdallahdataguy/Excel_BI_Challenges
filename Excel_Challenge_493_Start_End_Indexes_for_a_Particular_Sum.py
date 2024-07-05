# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7214840461939646464-BJMD/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_493 - Start End Indexes for a Particular Sum.xlsx'
df = pd.read_excel(file_path, skiprows=1, usecols='A:B')

# Perform data wrangling
start = 0
end = 1
values = []
for i in df.index:
    curr_sum = sum(df.iloc[start : end, 1])
    next_sum = sum(df.iloc[start : end + 1, 1])
    if start == max(df.index) or next_sum > 100:
        values.append([df.iat[start, 0], df.iat[end - 1, 0], curr_sum])
        start = end
    end += 1

df = pd.DataFrame(data=values, columns=['Start Index', 'End Index', 'Sum'])

# Display the final dataset
df
