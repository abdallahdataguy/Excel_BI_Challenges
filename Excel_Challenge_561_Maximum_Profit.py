# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7249629684731170817-DW8v/

from itertools import combinations

# Create a function to return the values
def get_values(row):
    combs = filter(lambda x: x[1] > x[0], combinations(row.values, 2))
    values = sorted(combs, key=lambda x: x[0] - x[1])
    if values:
        return list(values[0]) + [values[0][1] - values[0][0]]
    else:
        return ['NP', 'NP', 'NP']

# Read the data range
df = xl("A2:J11", headers=True)

# Perform data manipulation
df[['Buy', 'Sell', 'Profit']] = df.apply(get_values, axis=1).tolist()

df = df.iloc[:, -3:] # Get the last new columns

# Display the final results
df
