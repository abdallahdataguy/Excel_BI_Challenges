# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7192009978952507392-4Kil/

import pandas as pd

# Create a function to generate the required results
def inverted_triangle(n):
    values = []
    for i in range(n):
        start = i * (i + 1) // 2 + 1
        value = list(range(start, start + i + 1))
        value = value[::-1][:-1] + value
        empty = [''] * (((2 * n - 1) - len(value)) // 2)
        value = empty + value + empty
        values.insert(0, value)
    return values

# Create a dataframe of the results expected
df = pd.DataFrame(inverted_triangle(7))

# Display the output
df
