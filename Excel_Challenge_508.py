# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7222450587827601408-CPVS/

from math import isqrt, sqrt

# create a function to identify the required numbers
def is_perfect_sum_square(num):
    sum_digits_square = sum([int(x) ** 2 for x in str(num)])
    cond = isqrt(sum_digits_square) == round(sqrt(sum_digits_square), 9)
    return cond

# Create a function to generate a list of the first
# n numbers meeting the listed criteria
def generate_numbers(n):
    end_num = 1000
    while True:
        nums = map(lambda x: x ** 2, range(10, end_num))
        nums = list(filter(is_perfect_sum_square, nums))
        if len(nums) >= n:
            return nums[ : n]
        else:
            end_num *= 10

# Generate the list of the first 500 numbers
numbers = generate_numbers(500)

# Display the list
numbers
