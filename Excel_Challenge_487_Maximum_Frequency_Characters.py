# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7211941341545598976-BVqq/

import pandas as pd

# Create a function to generate the required results
def max_freq(text):
    max_occur = max([text.count(char) for char in set(text)])
    popular = [char for char in text if text.count(char) == max_occur]
    unique = [char for i, char in enumerate(popular) 
              if popular[: i + 1].count(char) == 1]
    return ', '.join(unique), max_occur

# Read the Excel file
file_path = 'Excel_Challenge_487 - Maximum Frequency Characters.xlsx'
df = pd.read_excel(file_path, skiprows=1)

# Perform data wrangling
df[['My Characters', 'My Frequency']] = df['Strings'].map(max_freq).tolist()

# Display the final dataset
df
