# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7208679833067806721-xS5S/

import pandas as pd

# Create a function to generate the required results
def decriptor(text, shift):
    decripted = ''
    for key, char in enumerate(text):
        num = ord(char) - (shift + key) % 26
        num = (
            num if char.isupper() == chr(num).isupper()
            else ord(char) + 26 - (shift + key) % 26
              )
        decripted += chr(num)
    return decripted

# Read the Excel file
file_path = "Caesar's Cipher_Decrypter.xlsx"
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df.apply(lambda x: decriptor(*x[: 2]), axis=1)
df['check'] = df['Answer Expected'] == df['My Answer']

# Display the final dataset
df
