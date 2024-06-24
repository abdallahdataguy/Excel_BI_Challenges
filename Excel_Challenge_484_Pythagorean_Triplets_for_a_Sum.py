# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7210854710818312193-bd_F/

import pandas as pd
from itertools import product

# Create a function to generate the required results
def pythagorean_triplet(number):
    numbers = []
    rng = range(1, number // 2)
    for i, j in product(rng, rng):
        t = (i ** 2 + j ** 2) ** 0.5
        if i + j + t == number:
            numbers = sorted([i, j, int(t)])
            break
    return numbers if numbers else ['None'] * 3

# Read the Excel file
file_path = 'Excel_Challenge_484 - Pythagorean Triplets for a Sum.xlsx'
df = pd.read_excel(file_path, usecols='A', skiprows=1)

# Perform data wrangling
df[['a', 'b', 'c']] = df['Sum'].map(pythagorean_triplet).tolist()

# Display the final datset
df
