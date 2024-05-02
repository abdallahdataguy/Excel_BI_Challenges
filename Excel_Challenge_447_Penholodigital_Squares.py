# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7191647594274603009-qodK/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_447 - Penholodigital Squares.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
digits = [str(x) for x in range(1, 10)]
interval = range(int(123456789 ** 0.5), int(987654321 ** 0.5) + 1)
numbers = [c for x in interval if all(item in list(str(c := x ** 2)) for item in digits) and len(str(c)) == 9]
df['My Answer'] = pd.Series(numbers)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Print the random sample output
print(f'Random sample of records:\n\n {df.sample(n=10, replace=False)}')
