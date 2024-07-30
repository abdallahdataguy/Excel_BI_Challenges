# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7223537760245055488-ZH8z/

# Create a function to generate the required results
def pascal_triangle(size):
    values = []
    rows = range(size)
    cols = range(size)
    for i in rows:
        value = []
        for j in cols:
            if i == 0:
                value = [0] * (size - 1) + [1]
                break
            if j == 0:
                value.append(1 if i == max(rows) else 0)
            else:
                value.append(values[-1][j - 1] + values[-1][j + 1])
        values.append(value + value[::-1][1:])
    results = [str(sum([x[i] for x in values])) for i in range(2 * size - 1)]
    return ', '.join(results)
    
# Read the data range
df = xl("A1:B5", headers=True)

# Perform data munging
df['My Answer'] = df['Rows'].map(pascal_triangle)

# Display the final results
df
