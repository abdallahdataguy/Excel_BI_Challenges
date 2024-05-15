# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7189110889139093505-xiKF/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_442 - Columnar Transposition Cipher.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def columnar_transposition_cipher(col1, col2):
    length = len(col2)
    col1 = col1.replace(' ', '')
    letters = list(col1) + [''] * (length - len(col1) % length)
    positions = [(x, y) for x, y in enumerate(col2, start=1)]
    positions.sort(key=lambda x: x[1])
    sort_values = [x[0] for x in positions]
    chars = []
    for ind, char in enumerate(letters, start=1):
        if not ind % length: chars.append([length, char])
        else: chars.append([ind % length, char])
    results = []
    for n in sort_values: results.append(''.join([s[1] for s in chars if s[0] == n]))
    return ' '.join(results)

df['My Answer'] = df.apply(lambda x: columnar_transposition_cipher(x['Plain Text'], x['Keyword']), axis=1)
df['Correct'] = df['Answer Expected'] == df['My Answer']

# Display the output
df
