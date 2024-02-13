# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7163018969207980032-7p29/

import pandas as pd

# Read an excel file
file_path = 'Excel_Challenge_390_Digit Equal to Sum of Digits.xlsx'
df = pd.read_excel(file_path)

# Create a custom function to generate the required results
def results(col):
    values = []
    value = 10 ** (col-1)
    while len(str(value)) == col:
        if sum([int(x) for x in str(value)]) == col:
            values.append(value)
        value += 1
    return (min(values), max(values), len(values))

# Add three columns in a go using the function defined above
df[['MyMin','MyMax','MyCount']] = df['Digits'].apply(results).tolist()

print(df)



