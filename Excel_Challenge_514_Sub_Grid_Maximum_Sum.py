# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7226074469004378112-U4Ka/

# Read the data range
df = xl("B2:F6", headers=False)

# Perform data wrangling
items = []
for i in df.index[:-1]:
    for j in range(len(df.columns)-1):
        values = list(df.iloc[i, j:j+2]) + list(df.iloc[i+1, j:j+2])
        row1 = ', '.join([str(x) for x in values[:2]])
        row2 = ', '.join([str(x) for x in values[2:]])
        total = sum(values)
        items.append([total, row1 + '; ' + row2])

max_total = max([item[0] for item in items])
result = [item[1] for item in items if item[0] == max_total]

# Display the final results
result
