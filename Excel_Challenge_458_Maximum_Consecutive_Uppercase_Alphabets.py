# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7197083411390304256-0WOz/

import pandas as pd
import re

# Create a function to generate the required results
def consecutive_uppercase(text):
    text = re.sub('[^A-Z]', ' ', text).split()
    text = [x for x in text if len(x) == max([len(y) for y in text])]
    return ', '.join(text)                                       
    
# Read the Excel file
file_path = 'Excel_Challenge_458 - Maximum Consecutive Uppercase Alphabets.xlsx'
df = pd.read_excel(file_path).replace(float('nan'), '')

# Perform data wrangling
df['My Answer'] = df['Words'].map(lambda x: consecutive_uppercase(x))
df['Check'] = df['Expected Answer'] == df['My Answer']

# Display the output
df
