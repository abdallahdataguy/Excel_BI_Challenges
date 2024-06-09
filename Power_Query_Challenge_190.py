# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7205414250305974273-Ynlk/

import pandas as pd
import re

# Create functions to be used for data wrangling
def cap(text):
    return re.sub('([A-Z])', lambda x: ' ' + x[1], text).strip()

def date(text):
    return '/'.join(re.findall('(\d{4})(\d{2})(\d{2})', text)[0][::-1])
    
# Read the Excel file
file_path = 'PQ_Challenge_190.xlsx'
df = pd.read_excel(file_path, usecols='A', nrows=2)

# Perform data wrangling
columns = ['Name', 'Org', 'City', 'From Date', 'To Date']

pattern = 'Name:(\w+)Org:(\w+)City:(\w+)FromDate:(\d+)ToDate:(\d+)'
df[columns] = df['Data'].map(lambda x: re.findall(pattern, x)[0]).tolist()
df[['Name', 'City']] = df.apply(lambda x: (cap(x[1]), cap(x[3])), axis=1).tolist()
df[['From Date', 'To Date']] = df.apply(lambda x: (date(x[4]), date(x[5])), axis=1).tolist()
df = df.iloc[:, 1:]

# Display the final dataset
df
