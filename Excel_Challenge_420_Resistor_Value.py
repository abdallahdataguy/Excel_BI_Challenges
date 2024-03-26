# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7178239246875377666-XtHM/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_420 - Resistor Value.xlsx'
df = pd.read_excel(file_path, usecols='B')
df['ind'] = df.index.astype(str) # Add color codes (numbers) column
df2 = pd.read_excel(file_path, usecols='D:E', nrows=9)

# Create a function to generate the required output
def resistor_value(dataframe, col):
    values = [col[i: i + 2] for i in range(0, len(col), 2)]
    for i in range(len((values))):
        for j in dataframe.index:
            if dataframe.iat[j, 0] == values[i]:
                values[i] = dataframe.iat[j, 1]
    values = ''.join(values)
    if values[-1] == '0':
        return values[: -1]
    else:
        return values[: -1] + '0' * int(values[-1])

# Add the results column to the dataset and print the output
df2['My Answer'] = df2.apply(lambda x: resistor_value(df, x['Color Bands']), axis=1)
print(df2)
