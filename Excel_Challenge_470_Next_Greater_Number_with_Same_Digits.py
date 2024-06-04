# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7203606404480262147-V2oK/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_469 - Next Greater Number with Same Digits.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
def next_greater_number(number):
    largest_num = int(''.join(sorted(str(number))[::-1]))
    if number == largest_num:
        return 'No such number'
    
    for num in range(number + 1, largest_num + 1):
        if sorted(str(num)) == sorted(str(number)):
            return num

df['My Answer'] = df['Number'].map(next_greater_number)
df['Check'] = df.iloc[:, 1] == df.iloc[:, 2]

# Display the results
df
