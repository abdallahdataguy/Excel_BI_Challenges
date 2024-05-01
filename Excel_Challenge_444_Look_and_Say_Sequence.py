# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7190560434779803648-wH-b/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_443 - Look and Say Sequence.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def look_say_sequence(col):
    number = str(col)
    numbers = []
    for i in range(4):
        digits = ''
        for num in number:
            if num not in digits:
                digits += num
        numbers.append(''.join([str(number.count(x)) + x for x in digits]))
        number = numbers[-1]
    return ', '.join(numbers)

df['My Answer'] = df['Numbers'].apply(look_say_sequence)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the output
df
