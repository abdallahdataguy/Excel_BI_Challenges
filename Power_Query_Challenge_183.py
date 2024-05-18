# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7197445811071291393-pVwj/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_183.xlsx'
df = pd.read_excel(file_path, usecols='A:F', nrows=4)
df1 = pd.read_excel(file_path, usecols='H:K') # Expected
df1.iloc[:, 3] = df1.iloc[:, 3].map(lambda x: round(x))

# Perform data wrangling
items = []
for i in df.index:
    v, h, r = df.iloc[i, [0, 5, 4]]
    for j in range(df.iat[i, 3]):
        y, q = df.iloc[i, [1, 2]]
        if j + int(q[1]) <= 4:
            items.append([v, y, 'Q' + str(j + int(q[1])), r])
        else:
            y = (df.iat[i, 1] + ((j + int(q[1])) // 4 - 1 
                                  if (j + int(q[1])) % 4 == 0 else (j + int(q[1])) // 4))
            q = 'Q4' if (j + int(q[1])) % 4 == 0 else 'Q' + str((j + int(q[1])) % 4)
            r = r * (1 + h / 100) if j % 4 == 0 else r
            items.append([v, y, q, r])

df = pd.DataFrame(items, columns=df.columns[[0, 1, 2, 4]]) # Computed
df['Rental'] = df['Rental'].map(lambda x: round(x))

# Check if my result equals the expected results
print(f'\nMy computed vs Expected results! Are they equal? {(df.values == df1.values).all()}')

# Display sample results 
df.sample(10)
