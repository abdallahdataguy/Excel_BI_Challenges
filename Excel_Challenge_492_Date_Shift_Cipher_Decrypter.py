# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7212303700009111553-JvMr/

import pandas as pd
from math import ceil

# Create a function to decrypt the text
def date_shift_cipher_decrypter(text, date):        
    date = str(date)
    shift = (date * ceil(len(text) / len(date)))[ : len(text)]
    decrypted_text = ''
    for key, char in enumerate(text):
        code = ord(char) - int(shift[key])
        decrypted_text += chr(code + 26 * (code < 97))
    return decrypted_text

# Read the Excel file
file_path = 'Excel_Challenge_492 - Date Shift Cipher Decrypter.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df.apply(
    lambda x: date_shift_cipher_decrypter(x['Message'], x['Key']), axis=1
)
df['Check'] = df['My Answer'] == df['Answer Expected']

# Display the final dataset
df
