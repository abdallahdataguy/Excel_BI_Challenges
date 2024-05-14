# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7195996261794091008-mLjS/

import pandas as pd

# Read the file
file_path = 'Excel_Challenge_455 - Anti perfect numbers.xlsx'
df = pd.read_excel(file_path, usecols ='A')
df1 = pd.read_excel(file_path, usecols ='B', nrows=4)
# Perform data transformation and cleansing
def is_anti_perfect_number(number):
    total = 0
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            if i == number / i:
                total += int(str(i)[::-1])
            else:
                total += (int(str(i)[::-1]) + int(str(number // i)[::-1]))
    return number == total + 1

df['My Answer'] = df['Numbers'][df['Numbers'].apply(is_anti_perfect_number)]
df2 = df['My Answer'].dropna(ignore_index=True).astype(int)
df = pd.concat([df1, df2], axis=1)

# Display Final Results
df
