# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7207955066543054848-2Q_9/

import pandas as pd

# Create functions to generate the required results
def schedule(df):
    values = []
    for i in df.index:
        if pd.notnull(df.iat[i, 1]):
            if df.iat[i + 1, 4] == df.iat[i, 4]: values.append('On Time')
            elif df.iat[i + 1, 4] > df.iat[i, 4]: values.append('Overrun')
            else: values.append('Underrun')
        else: values.append('')
    return values

def cost(df):
    values = []
    for i in df.index:
        if pd.notnull(df.iat[i, 1]):
            actual = len(pd.bdate_range(df.iat[i + 1, 3], df.iat[i + 1, 4]))
            plan = len(pd.bdate_range(df.iat[i, 3], df.iat[i, 4]))
            if actual == plan: values.append('At Cost')
            elif actual > plan: values.append('Overrun')
            else: values.append('Underrun')
        else: values.append('')
    return values
        
# Read the Excel file
file_path = 'PQ_Challenge_192.xlsx'
df = pd.read_excel(file_path, usecols='A:E')

# Perform data wrangling
df[['Schedule Performance', 'Cost Performance']] = list(zip(schedule(df), cost(df)))
df = df.dropna(subset='Phase', ignore_index=True).iloc[:, [0, 1, 5, 6]].fillna('')

# Display the final output
df
