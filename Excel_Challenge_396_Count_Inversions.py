# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7165918060598489088-F6va/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_396 - Count Inversions.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the required counts
def count_inversion(col):
    inversions = []
    for i in range(len(str(col)) - 1):
        for char in str(col)[i + 1:]:
            if str(col)[i] > char:
                inversions.append((str(col)[i], char))
    return len(inversions)

# Add new column to output the expected results using 
# the custom function created above
df['My Answer'] = df['String'].apply(count_inversion)

print(df)
