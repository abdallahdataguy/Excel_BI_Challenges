# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7194184330783404032-yDp4/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_452 - Parasitic Numbers.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
values = []
for x in range(1, 10 ** 6 + 1):
    for y in range(2, 10):
        if int(str(x)[-1] + str(x)[: -1]) == x * y and [x, y] not in values:
            values.append([x,y])
df[['MyNumber', 'MyMultiplier']] = values

# Display the results
df
