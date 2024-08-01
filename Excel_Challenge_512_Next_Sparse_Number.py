# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7224624946709200896-5QWi/

import pandas as pd

def min_sparse_after_number(number):
    start = number + 1
    while True:
        for num in range(start, start * 10):
            if '11' not in bin(num):
                return num
        start *= 10

# Read the data range
df = xl("A1:B10", headers=True)

# Perform data munging
df['My Answer'] = df['Number'].map(min_sparse_after_number)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
