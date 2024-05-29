# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7201432095284465664-QZ_G/

import pandas as pd
import numpy as np

# Read the Excel file
file_path = 'Excel_Challenge_466 - Bouncy Numbers.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
def bouncy_numbers(n):
    number, numbers = 10, []
    while len(numbers) < n:
        a = np.array(list(str(number)[1 : ]), int)
        b = np.array(list(str(number)[ : -1]), int)
        if not all(a >= b) + all(a <= b):
            numbers.append(number)
        number += 1
    return numbers

df['My Answer'] = bouncy_numbers(10000) 
df['Check'] = df.iloc[: , 0] == df.iloc[: , 1]
                
# Display the final results
df
