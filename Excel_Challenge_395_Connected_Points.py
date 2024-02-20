# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7165555694702727169-2xxk/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_395 - Connected Points.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the required output
def connected_points(col1, col2, col3, col4):
    values = [x for x in (col1, col2, col3, col4) if pd.notnull(x)]
    value, step = True, 0 
    while step < len(values) - 1:
        value = value and values[step].split(', ')[1] == values[step + 1].split(', ')[0]
        step += 1
    return 'Yes' if value else 'No'

# Add new results column to the dataframe and print the output
df['My Answer'] = df.apply(lambda x: connected_points(x['Coord1'], x['Coord2'], x['Coord3'], x['Coord4']), axis=1)

print(df)
