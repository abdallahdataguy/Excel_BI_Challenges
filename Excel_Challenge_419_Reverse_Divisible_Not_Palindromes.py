# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7177876857915117569-cHiT/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_419 - Reverse Divisible & Not Palindromes.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the required results
def reverse_divisible_not_palindrome(n):
    numbers = []
    number = 10
    while len(numbers) != n:
        rev_number = int(str(number)[::-1])
        value = rev_number / number
        if value == int(value) and number != rev_number:
            numbers.append(number)
        number += 1
    return numbers

# Add a column to show the desired output
df['My Answer'] = pd.Series(reverse_divisible_not_palindrome(11))

# Print the output
print(df)
