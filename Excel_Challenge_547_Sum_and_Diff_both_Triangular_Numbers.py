# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7242381897509556224-K2YI/

from itertools import combinations

# Create a function to categorize numbers 
# as either triangulars or not
def is_triang(num):
    s = ((8 * num + 1) ** 0.5 - 1)/2
    return s == int(s)

# Perform data manipulation   
triangulars = map(lambda n: n * (n + 1) // 2, range(1, 2000))
pairs = filter(
    lambda n: is_triang(sum(n)) and is_triang(abs(n[0]-n[1])), 
    combinations(triangulars, 2)
)
pairs = sorted(set(map(lambda n: tuple(sorted(n)), pairs)))[:20]
pairs = [', '.join(map(str, n)) for n in pairs]

# Display the final results
pairs
