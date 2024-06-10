# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7205780719636213760-Xn2N/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_474 - Wavy Numbers.xlsx'
df1 = pd.read_excel(file_path, usecols='A')
df =  pd.read_excel(file_path, usecols='B', nrows=5)

# Perform data wrangling
numbers = []
for number in df1['Numbers']:
    nums = list(str(number))
    if all([(nums[i - 1] < nums[i] > nums[i + 1]) 
            or (nums[i - 1] > nums[i] < nums[i + 1]) 
            for i in range(1, len(nums) - 1)]):
        numbers.append(number)

df['My Answer'] = numbers

# Display the final dataset
df
