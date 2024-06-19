# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7209047298738184192-Dm5z/

import pandas as pd
from itertools import product

# Create a function to generate the reqired output
def is_taxicab_number(number):
    numbers = []
    values = range(1, int(number ** (1/3)) + 1)
    for num1, num2 in product(values, values):
        if num1 != num2 and num1 ** 3 + num2 ** 3 == number:
            numbers.extend([num1, num2])
    return 'Y' if len(set(numbers)) > 2 else 'N'

# Read the Excel file
file_path = 'Excel_Challenge_481 - Taxicab Numbers.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df['Numbers'].map(is_taxicab_number)
df['check'] = df['Answer Expected'] == df['My Answer']

# Display the final dataset
df
