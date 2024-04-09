# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7183312674775068674-K_xZ/

import pandas as pd

# Generate the required output
n = 26
letters = [chr(x) for x in range(n + 64, n + 38, -1)]
values = []
for i in range(1, n + 1):
    values.append([''] * (n - i + 1) + letters[i - 1: ] + [''] * (i - 1) )

df = pd.DataFrame(values)

# Save the dataframe as an Excel to disk
df.to_excel('Excel_Challenge_430 - Alphabetic Searchlight.xlsx', index=False)

# Print the sample output
print(df.iloc[:26, :26])
