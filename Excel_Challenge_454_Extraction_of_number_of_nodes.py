# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7195633858837434368-Ikp9/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_454 - Extraction of number of nodes.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def count_extracted_numbers(col):
    numbers = 0
    s = col.lower().replace(' to ', '-').split(' ')
    for a in s:
        if a.find('-') == -1: numbers += 1
        else: numbers += 1- eval(a)
    return numbers

df['My Answer'] = df['Pronlem'].apply(count_extracted_numbers)

# Display the results
df
