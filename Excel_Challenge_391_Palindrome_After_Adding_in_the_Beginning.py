# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7163381340954845185-UHGU/

import pandas as pd

# Read an Excel file
file_path = 'Excel_Challenge_391- Palindrome After Adding in the Beginning.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the required results
def make_palindrome(col):
    value = col
    if value == value[::-1]:
        return value
    for i in range(-1, -len(col), -1):
        test = col[i:][::-1] + value
        if test == test[::-1]:
            value = test
            break
    return value

# Add new column by applying the function created above 
df['My Answer'] = df['String'].apply(make_palindrome)
    
print(df)
