# Link to the challenge
# https://www.linkedin.com/feed/update/urn:li:activity:7161931798501867520/

import pandas as pd
import re

# Read the file
file_path = 'Power_Query_Challenge_155.xlsx'
df = pd.read_excel(file_path, usecols=[0, 3])

# Create a function to extract valid times from a string
def extract_valid_times(col):
    valid_times = [x for x in re.findall(r'\d{1,2}:\d{2}', col) 
                     if int(x.split(':')[0]) < 24 and int(x.split(':')[1]) < 60]
    return ', '.join(valid_times)

# Create a new column using a user defined function above
df['My Answer'] = df['String'].apply(extract_valid_times)

# Replace empty string values by na values
df['My Answer'] = df['My Answer'].replace('', float('nan'))

print(df)
