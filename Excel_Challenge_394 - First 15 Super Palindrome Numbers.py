# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7165193277124677632-QC3m/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_394 - First 15 Super Palindrome Numbers.xlsx'
df = pd.read_excel(file_path, usecols='A')

# Create functions to generate the required output
def is_palindrome(number):
    return str(number) == str(number)[::-1]

def super_palindrome(n):
    numbers = []
    number = 10
    while len(numbers) < n:
        sqrt_num = number ** 0.5
        if is_palindrome(number) and is_palindrome(int(sqrt_num)) and sqrt_num == int(sqrt_num):
            numbers.append(number)
        number += 1
    return numbers

# Add new column using the functions above
df['My Answer'] = pd.Series(super_palindrome(15))

print(df)
