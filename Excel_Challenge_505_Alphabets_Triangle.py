# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7221363400465870848-la-j/

from string import ascii_uppercase

# Create a function to generate a triangle 
# of the first n alphabets. By default n = 26
def gen_alphabets_triangle(n=26):
    chars = ascii_uppercase[: n]
    maximum = [i for i in range(n) if (i ** 2 - i + 2) // 2 < n][-1]
    values = []
    for i in range(1, maximum + 1):
        start = (i ** 2 - i + 2) // 2 - 1
        end  = start + i
        a = '  '.join([char for char in chars[start : end]]).split(' ')
        b = [''] * ((maximum * 2 - len(a) - 1) // 2)
        values.append(b + a + b)
    return values

# Perfom data munging
lst = gen_alphabets_triangle()
    
# Display the final results
lst
