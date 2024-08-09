# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7226799223977967617-PDsu/

from itertools import combinations_with_replacement
from functools import reduce
from string import digits

# Create a function  to generate the required result
def get_min_product(number):
    for i in range(2, 10):
        values =[
            int(''.join(x)) for x in combinations_with_replacement(digits[1:], i) 
            if reduce(lambda a, b: int(a) * int(b), x) == number
        ]
        if values:
            return min(values)
    return 'NP'

# Read the data range
df = xl("A1:B10", headers=True)

# Perform data munging
df['My Answer'] = df['Number'].map(get_min_product)
            
# Display the final results
df
