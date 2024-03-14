# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7173890586880458752-rEx5/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_412 - Square Sum Iterate till a Single Digit .xlsx'
df = pd.read_excel(file_path, usecols='A', skiprows=1)
df_test = pd.read_excel(file_path, usecols='A:C', skiprows=1)

# Create a function to generate the required output
def single_digit(number):
    value, n = sum([int(x) ** 2 for x in str(number)]), 1
    while len(str(value)) != 1:
        value = sum([int(x) ** 2 for x in str(value)])
        n += 1
    return value, n

# Add results columns using the devised formula
df[['Final Single Digit', 'Number of Iterations']] = df['Number'].apply(single_digit).tolist()

# print the dataframes for comparing outputs
print(f'Original results:\n{df_test}\n\nMy Results:\n{df}')
