# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7227161616620896257-cpK2/

import pandas as pd
from math import sqrt, isqrt

# Read the data range
df = xl("A1:B10", headers=True)

# Perform data munging
items = []
values = df['Numbers'].tolist()
while len(items) != len(values):
    num1 = items[-1] if items else values[0]
    num2 = [
        x for x in values if x != num1 and x not in items
        and sqrt(x + num1) == isqrt(x + num1)
    ]
    if items and num2:
        items += [num2[0]]
    else:
        items += [num2[0], num1]

df['My Answer'] = items

# Display the final results
df
