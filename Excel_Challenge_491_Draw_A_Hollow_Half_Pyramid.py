# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7214123690890813440-lcBk/

import pandas as pd

def gen_hollow_half_pyramid(n):
    values = []
    for r in range(1, n + 1):
        row = []
        for c in range(1, n + 1):
            if c == 1 or r == n or r == c:
                row.append(c if r == n else r)
            else:
                row.append("")
        values.append(row)
    return values

# Create the DataFrame
df = pd.DataFrame(gen_hollow_half_pyramid(8))

# Display the DataFrame
df
