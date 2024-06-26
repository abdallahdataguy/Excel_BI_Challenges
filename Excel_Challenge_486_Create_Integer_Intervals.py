# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7211578968074797057-Y1X4/

import pandas as pd

# Create a function to generate the required results
def integer_interval(text):
    numbers = list(map(int, text.split(', ')))
    values = []
    start = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            if start == numbers[i - 1]:
                values.append(f'{start}')
            else:
                values.append(f'{start}-{numbers[i - 1]}')
            start = numbers[i]
    
    # Handle the last interval
    if start == numbers[-1]:
        values.append(f'{start}')
    else:
        values.append(f'{start}-{numbers[-1]}')

    return ', '.join(values)
        
# Read the Excel file
file_path = 'Excel_Challenge_486 - Create Integer Intervals.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df['Problem'].map(integer_interval)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
