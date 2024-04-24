# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7188386131313385472-ehnR/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_440 - List of Numbers Expressed as Sum of Two Squares.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def sum_of_two_squares(start, end):
    numbers = []
    for i in range(start, end + 1):
        squares = [x for x in range(1, i + 1) if x ** 0.5 == int(x ** 0.5)]
        values = 0
        for j in squares:
            for k in [n for n in squares if n != j]:
                if j + k == i:
                    values += 1
        if values > 1:
            numbers.append(i)
    return numbers
    
df['My Answer'] = pd.Series(sum_of_two_squares(1, 100))

# Print the output
print(df)
