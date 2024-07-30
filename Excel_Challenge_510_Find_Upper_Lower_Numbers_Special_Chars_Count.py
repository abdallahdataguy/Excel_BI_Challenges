# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7223900132868517888-5dv_/

import re

# Create a function to generate the required results
def count_chars(text):
    if not text:
        return (0, 0, 0, 0)
    upper_case = len(re.findall('[A-Z]', text))
    lower_case = len(re.findall('[a-z]', text))
    numbers = len(re.findall('\d', text))
    special = len(re.findall('[_\W]', text))
    return upper_case, lower_case, numbers, special

# Read the data range
df = xl("A2:A12", headers=True)

# Perform data munging
df = df.replace(np.nan, '')
df[
    ['Upper Case', 'Lower Case', 'Numbers', 'Special Chars']
] = df['Data'].map(count_chars).tolist()

# Display the final results
df
