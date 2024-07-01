# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7213390875882602498-SzOL/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_489 - Total Time in a Week.xlsx'
df = pd.read_excel(file_path, skiprows=1, usecols='A:H')

# Perform data wrangling
names = [x for y in df.iloc[:, 1:].values for x in y if not pd.isna(x)]
names = [name for key, name in enumerate(names) if names[ : key + 1].count(name) == 1]

items = []
for name in names:
    total = 0
    for i in df.index:
        record = df.iloc[i].tolist()
        Times = record[0].replace(':', '.').replace('30', '5').split(' - ')
        name_count = record.count(name)
        total += name_count * (float(Times[1]) - float(Times[0]))
    items.append([name, total])

df = pd.DataFrame(data=items, columns=['Name', 'Total Hours'])

# Display the final dataset
df
