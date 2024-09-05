# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7237308493429387264-HC2L/

from itertools import combinations
from functools import reduce

# Create a function to generate the min product
def get_min_product(row):
    products = [
        reduce(lambda x, y: x * y, comb) 
        for comb in combinations(row[:-1], 3)
    ]
    return min(products)
    
# Read the data range
df = xl("A1:G10", headers=True)

# Perform data munging
df['My Answer'] = df.apply(get_min_product, axis=1)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
