# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7175340145666105345-WjkF/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_414 - IMO Number of a Vessel.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Create a function to generate the required results
def complete_imo_number(number):
    values = []
    sequence = range(7,1,-1)
    for i in range(10):
        new_number = number.replace('X', str(i))
        total = 0
        for j in range(6):
            total += int(new_number[j]) * sequence[j]
        if str(total)[-1] == new_number[-1]:
            values.append(new_number)
    return ', '.join(values)

# Add results column by using the function created above
df['My Answer'] = df['IMO Number'].apply(complete_imo_number)

# Print the output. The question has many results more than the listed
print(df)

