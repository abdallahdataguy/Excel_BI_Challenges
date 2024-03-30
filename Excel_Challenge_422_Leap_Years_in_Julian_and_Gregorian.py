# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7178964017565032448-lzFX/

import pandas as pd

file_path = 'Excel_Challenge_422 - Leap Years in Julian and Gregorian.xlsx'
df = pd.read_excel(file_path)

def revised_julian_leap_year(number):
    if not number % 4:
        if not number % 100: return number % 900 in (200, 600)
        else: return True

def gregorian_leap_year(number):
    if not number % 4:
        if not number % 100: return not number % 400
        else: return True

def leap_julian_xor_gregorian(numbers):
    values = []
    for number in numbers:
        a = revised_julian_leap_year(number)
        b = gregorian_leap_year(number)
        if a != b:
            values.append(number)
    return values

df['My Answer'] = pd.Series(leap_julian_xor_gregorian(range(1901, 10000)))
print(df)
