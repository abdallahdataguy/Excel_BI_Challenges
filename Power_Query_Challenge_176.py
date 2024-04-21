# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7187661342286237696-tA5J/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_176.xlsx'
df = pd.read_excel(file_path, usecols='A:C', nrows=4)

# Perform data transformation and cleansing
values = []
for i in df.index:
    x = df.iat[i , 0]
    y = df.iat[i , 1].split(', ')
    z = [int(a) for a in df.iat[i , 2].split(', ')]
    total = 0
    for j in range(len(y)):
        try: total += z[j]
        except: ''
        values.append([x, y[j], total]) 

df = pd.DataFrame(values)
df.columns = ['Group', 'Column1', 'Column2']

# Print the output
print(f'\nFinal results:\n\n{df}')
