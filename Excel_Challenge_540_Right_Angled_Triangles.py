# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7239120428235915264-3zXz/

from itertools import combinations

# Create a function to generate the required results
def get_perp_base(row):
    items = row.values
    for comb in combinations(range(1, items[0]), 2):
        cond1 = 0.5 * comb[0] * comb[1] == items[1]
        cond2 = comb[0] ** 2 + comb[1] ** 2 == items[0] ** 2
        if cond1 and cond2:
            return comb
    return 'NP', 'NP'

# Read the data range
df = xl("A2:B10", headers=True)

# Perform data manipulation  
df[['Perpendicular', 'Base']] = df.apply(get_perp_base, axis=1).tolist()

# Display the final results
df
