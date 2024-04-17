# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7186211807747862528-KTXO/

import pandas as pd

# Create functions to generate the required results
def is_prime(number):
    if number < 2: 
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0: 
            return False
    return True

def is_pandigital(number):
    available_digits = [int(x) for x in str(number)]
    expected_digits = list(range(1, len(str(number)) + 1))
    return expected_digits == sorted(available_digits)

def prime_pandigital(n):
    numbers = []
    number = 10
    while len(numbers) < n:
        if is_prime(number) and is_pandigital(number):
            numbers.append(number)
        number += 1
    return numbers

# Read the Excel file and add a computed column
file_path = 'Excel_Challenge_436 - Pandigital Primes.xlsx'
df = pd.read_excel(file_path)
df['My Answer'] = pd.Series(prime_pandigital(100))

# Print the output
print(f'\nRequired Results:\n{df}')
