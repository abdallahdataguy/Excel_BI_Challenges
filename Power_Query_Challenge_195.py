# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7212665760391843840-7CLQ/

import pandas as pd

# Function to clean and split text into alphanumeric words
def clean_split(text):
    for char in text:
        if not char.isalpha() and not char.isdigit():
            text = text.replace(char, ' ')
    return text.split()

# Read the Excel file
file_path = 'PQ_Challenge_195.xlsx'
df1 = pd.read_excel(file_path, usecols='A:C', nrows=4).astype(str)
df2 = pd.read_excel(file_path, usecols='A:B', skiprows=7)

# Perform data wrangling
df2['Items'] = df2['Items'].map(lambda x: x.split(', '))
df2 = df2.explode(column='Items', ignore_index=True)
df2['Count'] = df2.groupby('Items').transform('count')

# Apply clean_split function to each column in df1
for col in df1.columns:
    df1[col] = df1[col].map(clean_split)

df1 = df1.explode(column=['Items', 'Unit Price', 'Quantity'], ignore_index=True)
df = df2.merge(df1)
df[df.columns[2: ]] = df[df.columns[2: ]].astype(int)
df['Amount Paid'] = df.apply(lambda x: x[3] * x[4] /x[2], axis=1).astype(int)
df = df.groupby('Stockist')['Amount Paid'].sum().reset_index()

# Display the final dataset
df
