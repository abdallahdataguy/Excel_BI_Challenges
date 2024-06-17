# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7208317458225520640-pfrA/

import pandas as pd

# Create a function to generate the required sequence of numbers
def recaman_sequence(size):
    numbers = [0]
    n = 1
    while len(numbers) < size:
        num = numbers[-1]
        if num - n > 0 and num - n not in numbers:
            numbers.append(num - n)
        else:
            numbers.append(num + n)
        n += 1
    return numbers

# Read the Excel file
file_path = 'Excel_Challenge_479 - Recaman Sequence.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = recaman_sequence(len(df))
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
