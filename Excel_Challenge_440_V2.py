# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7188386131313385472-ehnR/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_440 - List of Numbers Expressed as Sum of Two Squares.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def sum_of_two_squares(start, end):
    values =  []
    for i in range(1, end + 1):
        for j in [n for n in range(1, end + 1) if n != i]:
            total = i ** 2 + j ** 2
            if start <= total <= end:
                values.append(total)
    return sorted(list(set(values)))

df['My Answer'] = pd.Series(sum_of_two_squares(1, 100))

# Print the output
print(df)
