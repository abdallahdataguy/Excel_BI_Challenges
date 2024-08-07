# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7206140862215499776-5Y00/

import pandas as pd

# Create a function to split the text
def split_by_positions(text, pos):
    starts = [0] + [int(x) - 1 for x in str(pos).split(',')]
    ends = starts[1 : ] + [len(text)]
    splits = [text[x : y] for x, y in zip(starts, ends)]
    
    return splits

# Read the Excek file
file_path = 'Excel_Challenge_475 - Split by Positions.xlsx'
df = pd.read_excel(file_path, usecols='A:B', skiprows=1)

# Perform data wrangling
df = pd.DataFrame(df.apply(lambda x: split_by_positions(x[0], x[1]), axis=1).tolist())
df.columns = ['Text' + str(x + 1) for x in df.columns]
df = df.fillna('')

# Display the final dataset
df
